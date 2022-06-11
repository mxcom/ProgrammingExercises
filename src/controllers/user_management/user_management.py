import datetime
from src.controllers.cryptography.cryptography import hash_passwd, compare_passwd
from src.controllers.database.database import Database
from src.models.user_management.user import User
from src.controllers.user_management.calc_kcal import calc_kcal


def add_user(user):
    global id
    db = Database()
    cursor = db.get_cursor()
    cursor.execute("INSERT INTO user (Email, FirstName, LastName, Sex, Birthday, Height, Password)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s);",
                   (user.get_email(), user.get_first_name(), user.get_last_name(), user.get_sex(),
                    datetime.datetime.strptime(user.get_birthday().replace(".", "-"), '%d-%m-%y'), int(user.get_height()),
                    hash_passwd(user.get_passwd())))
    cursor.execute("SELECT UserID FROM user WHERE Email LIKE %s;", (user.get_email(),))
    date = datetime.datetime.now().date().strftime("%Y-%m-%d")
    print(date)
    data = cursor.fetchall()
    for i in data:
        id = i[0]
    cursor.execute("INSERT INTO weight (UserID, Grams, TrackDate)"
                   " VALUES (%s, %s, %s);",
                   (id, user.get_weight(), date))
    db.get_database().close()


def get_user(email):
    try:
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("SELECT * FROM user WHERE Email LIKE %s;", (email,))
        user = User()
        for i in cursor.fetchall():
            user.set_id(i[0])
            user.set_email(i[1])
            user.set_first_name(i[2])
            user.set_last_name(i[3])
            user.set_sex(i[4])
            user.set_birthday(i[5])
            user.set_height(i[6])
            user.set_passwd(i[7])
        cursor.execute("SELECT Grams FROM weight JOIN user u on weight.UserID = u.UserID WHERE u.Email = %s;", (email,))
        for i in cursor.fetchall():
            user.set_weight(i[0])
        db.get_database().close()
        return user
    except Exception as e:
        print(e)
        return False


def add_steps(id, steps):
    try:
        db = Database()
        cursor = db.get_cursor()
        date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO steps (UserID, Steps, Date)"
                       "VALUES (%s, %s, %s);",
                       (id, steps, date))
        db.get_database().close()
    except Exception as e:
        print(e)


def add_weight(id, weight):
    try:
        db = Database()
        cursor = db.get_cursor()
        date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO weight (UserID, Grams, TrackDate)"
                       "VALUES (%s, %s, %s);",
                       (id, weight, date))
        db.get_database().close()
    except Exception as e:
        print(e)


def add_bp(id, low, high):
    try:
        db = Database()
        cursor = db.get_cursor()
        date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO bloodpressure (UserID, Diastolic, Systolic, Date)"
                       "VALUES (%s, %s, %s, %s);",
                       (id, low, high, date))
        db.get_database().close()
    except Exception as e:
        print(e)

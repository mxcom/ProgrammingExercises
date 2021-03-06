import datetime
import random

from src.controllers.cryptography.cryptography import hash_passwd, compare_passwd
from src.controllers.database.database import Database
from src.models.user_management.user import User
from src.controllers.user_management.calc_kcal import calc_kcal
from src.controllers.primary.daily_track import DailyTrack


def add_user(user):
    global id
    db = Database()
    cursor = db.get_cursor()
    cursor.execute("INSERT INTO user (Email, FirstName, LastName, Sex, Birthday, Height, Password)"
                   "VALUES (%s, %s, %s, %s, %s, %s, %s);",
                   (user.get_email(), user.get_first_name(), user.get_last_name(), user.get_sex(),
                    user.get_birthday(), int(user.get_height()), hash_passwd(user.get_passwd())))
    cursor.execute("SELECT UserID FROM user WHERE Email LIKE %s;", (user.get_email(),))
    date = datetime.datetime.now().date().strftime("%Y-%m-%d")
    data = cursor.fetchall()
    for i in data:
        id = i[0]
    cursor.execute("INSERT INTO weight (UserID, Grams, Date)"
                   " VALUES (%s, %s, %s);",
                   (id, user.get_weight(), date))
    cursor.execute("INSERT INTO bloodpressure (UserID, Systolic, Diastolic, Date)"
                   " VALUES (%s, %s, %s, %s);",
                   (id, 0, 0, date))
    cursor.execute("INSERT INTO steps (UserID, Steps, Date)"
                   " VALUES (%s, %s, %s);",
                   (id, 0, date))
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

        cursor.execute("SELECT * FROM steps WHERE UserID LIKE %s AND Date LIKE %s;",
                       (id, date))

        current_steps = None
        for i in cursor.fetchall():
            current_steps = i[2]

        total = steps + current_steps
        cursor.execute("UPDATE steps SET steps = %s WHERE UserID LIKE %s AND Date LIKE %s",
                       (total, id, date))
        db.get_database().close()
    except Exception as e:
        print(e)


def add_weight(id, weight):
    try:
        db = Database()
        cursor = db.get_cursor()
        date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        cursor.execute("UPDATE weight SET Grams = %s WHERE UserID LIKE %s and Date LIKE %s;",
                       (weight, id, date))
        db.get_database().close()
    except Exception as e:
        print(e)


def add_bp(id, low, high):
    try:
        db = Database()
        cursor = db.get_cursor()
        date = datetime.datetime.now().date().strftime("%Y-%m-%d")
        cursor.execute("UPDATE bloodpressure SET Diastolic = %s, Systolic = %s WHERE UserID LIKE %s AND DATE LIKE %s;",
                       (low, high, id, date))
        db.get_database().close()
    except Exception as e:
        print(e)


def update_email(user, new_email):
    try:
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("UPDATE user SET Email = %s WHERE Email LIKE %s;", (new_email, user.get_email()))
        db.get_database().close()
        return True
    except Exception as e:
        print(e)
        return False


def update_passwd(user, new_passwd):
    try:
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("UPDATE user SET Password = %s WHERE UserID LIKE %s", (hash_passwd(new_passwd), user.get_id()))
        db.get_database().close()
        return True
    except Exception as e:
        print(e)
        return False


def update_height(user, new_height):
    try:
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("UPDATE user SET Height = %s WHERE UserID LIKE %s", (int(new_height), user.get_id()))
        db.get_database().close()
        return True
    except Exception as e:
        print(e)
        return False


def get_all_users():
    try:
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("SELECT * FROM user")

        users = []
        for i in cursor.fetchall():
            users.append(
                {"ID": str(i[0]), "Email": str(i[1]), "FirstName": str(i[2]), "LastName": str(i[3]), "Sex": str(i[4]),
                 "Birthday": str(i[5]),
                 "Height": str(i[6]), "Password": str(i[7])})
        return users
    except Exception as e:
        print(e)
        return None


def insert_random():
    try:
        db = Database()
        cursor = db.get_cursor()
        date = datetime.datetime.now()
        for i in range(100):
            date = date - datetime.timedelta(1)
            cursor.execute("INSERT INTO steps (UserID, Steps, Date) "
                           "VALUES (55, %s, %s)", (random.randint(5000, 12000), date.strftime("%Y-%m-%d")))

    except Exception as e:
        print(e)


def update_first_name(user, name):
    try:
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("UPDATE user SET FirstName = %s WHERE UserID LIKE %s", (name, user.get_id()))
    except Exception as e:
        print(e)


def update_last_name(user, name):
    try:
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("UPDATE user SET LastName = %s WHERE UserID LIKE %s", (name, user.get_id()))
    except Exception as e:
        print(e)


def update_sex(user, sex):
    try:
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("UPDATE user SET Sex = %s WHERE UserID LIKE %s", (sex, user.get_id()))
    except Exception as e:
        print(e)


def update_birthday(user, date):
    try:
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("UPDATE user SET Birthday = %s WHERE UserID LIKE %s", (date, user.get_id()))
    except Exception as e:
        print(e)


def update_height(user, height):
    try:
        db = Database()
        cursor = db.get_cursor()
        cursor.execute("UPDATE user SET Height = %s WHERE UserID LIKE %s", (height, user.get_id()))
    except Exception as e:
        print(e)


def login(user):
    try:
        db = Database()
        cursor = db.get_cursor()
        date = datetime.datetime.now().date().strftime("%Y-%m-%d")

        cursor.execute("INSERT INTO steps (Steps, Date, UserID) "
                       "SELECT %s, %s, %s FROM DUAL "
                       "WHERE NOT EXISTS (SELECT * FROM steps WHERE Date=%s AND UserID=%s LIMIT 1);",
                       (0, date, user.get_id(), date, user.get_id()))

        cursor.execute("INSERT INTO calories (Calories, CaloriesEaten, Date, UserID) "
                       "SELECT %s, %s, %s, %s FROM DUAL "
                       "WHERE NOT EXISTS (SELECT * FROM calories WHERE Date=%s AND UserID=%s LIMIT 1);",
                       (calc_kcal(user.get_sex(), user.get_height(), user.get_weight(), user.get_birthday()), 0, date,
                        user.get_id(), date, user.get_id()))

        cursor.execute("INSERT INTO bloodpressure (Diastolic, Systolic, Date, UserID) "
                       "SELECT %s, %s, %s, %s FROM DUAL "
                       "WHERE NOT EXISTS (SELECT * FROM bloodpressure WHERE Date=%s AND UserID=%s LIMIT 1);",
                       (0, 0, date, user.get_id(), date, user.get_id()))

        cursor.execute("INSERT INTO weight (Grams, Date, UserID) "
                       "SELECT %s, %s, %s FROM DUAL "
                       "WHERE NOT EXISTS (SELECT * FROM weight WHERE Date=%s AND UserID=%s LIMIT 1);",
                       (0, date, user.get_id(), date, user.get_id()))

    except Exception as e:
        print(e)


def get_food_from_date(date, user):
    track = DailyTrack()
    try:
        db = Database()
        cursor = db.get_cursor()
        cursor.execute(
            "SELECT calories.CaloriesEaten, steps.Steps, weight.Grams, bloodpressure.Diastolic, bloodpressure.Systolic "
            "FROM calories, steps, weight, bloodpressure "
            "WHERE calories.UserID LIKE %s AND calories.Date LIKE %s "
            "AND steps.UserID LIKE %s AND steps.Date LIKE %s "
            "AND weight.UserID LIKE %s AND weight.Date LIKE %s "
            "AND bloodpressure.UserID LIKE %s AND bloodpressure.Date LIKE %s",
            (user.get_id(), date, user.get_id(), date, user.get_id(), date, user.get_id(), date))

        for i in cursor.fetchall():
            bp = str(i[3]) + "/" + str(i[4])
            track.set_calories_eaten(i[0])
            track.set_steps_walked(i[1])
            track.set_weight(i[2])
            track.set_bloodpressure(bp)

        cursor.execute("SELECT food.Name, food.Calories, food_track.Count FROM food_track "
                       "INNER JOIN food on food_track.FoodID = food.FoodID "
                       "INNER JOIN calories on food_track.CaloriesID = calories.CaloriesID "
                       "INNER JOIN user u on calories.UserID = u.UserID "
                       "WHERE u.UserID LIKE %s AND calories.Date LIKE %s;",
                       (user.get_id(), date))

        food_amount = {}

        for i in cursor.fetchall():
            food_amount.update({i[0]: [i[1], i[2]]})

        track.set_food(food_amount)

        return track
    except Exception as e:
        print(e)

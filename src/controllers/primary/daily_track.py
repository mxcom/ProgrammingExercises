class DailyTrack:

    def __init__(self, calories_eaten="", steps_walked="", weight="", bloodpressure="", _food_amount=None):
        if _food_amount is None:
            _food_amount = {}
        self._calories_eaten = calories_eaten
        self._steps_walked = steps_walked
        self._weight = weight
        self._bloodpressure = bloodpressure
        self._food_amount = _food_amount

    def get_calories_eaten(self):
        return self._calories_eaten

    def get_steps_walked(self):
        return self._steps_walked

    def get_weight(self):
        return self._weight

    def get_bloodpressure(self):
        return self._bloodpressure

    def get_food(self):
        return self._food_amount

    def set_calories_eaten(self, calories_eaten):
        self._calories_eaten = calories_eaten

    def set_steps_walked(self, steps_walked):
        self._steps_walked = steps_walked

    def set_weight(self, weight):
        self._weight = weight

    def set_bloodpressure(self, bloodpressure):
        self._bloodpressure = bloodpressure

    def set_food(self, _food_amount):
        self._food_amount = _food_amount
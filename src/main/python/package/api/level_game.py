# easy game setup
from package.api.tools import generate_random_list, match_number, stopwatch


class Easy:
    # number of essai : 3
    # list len : 5
    # interval : [0,10]  with 0 and without 10
    def __init__(self):
        self.number_essai = 3
        self.list_len = 5
        self.interval = {"start": 0, "end": 10}
        self.random_list = generate_random_list(self.list_len,
                                                self.interval.get("start"),
                                                self.interval.get("end"))
        self.the_number = match_number(self.random_list)


# medium game setup
class Medium:
    # number of essai : 4
    # list len : 10
    # interval : [-9,10] with -9 and without 10
    def __init__(self):
        self.number_essai = 4
        self.list_len = 10
        self.interval = {"start": -9, "end": 10}
        self.random_list = generate_random_list(self.list_len,
                                                self.interval.get("start"),
                                                self.interval.get("end"))
        self.the_number = match_number(self.random_list)

import random
import time


def stopwatch(sec=0, minute=0, hour=0):
    sec_ = sec
    minute_ = minute
    hour_ = hour
    total_second = sec_ + (minute_ * 60) + (hour_ * 3600)
    futur = time.time() + total_second
    while time.time() < futur:
        pass
    return 0


# return a random list of element in an interval
def generate_random_list(list_len: [int], start_interval: int, end_interval: int):
    random_list = []
    while len(random_list) < list_len:
        current_random = random.randrange(start_interval, end_interval)
        if current_random in random_list:
            pass
        else:
            random_list.append(current_random)
    return random_list


# retun int. Verify if user entry is a integer
def give_number(message: str):
    message_ = message
    while True:
        answer = input(f"{message_}")
        if answer.isdigit():
            return int(answer)


# return true or false. Generate random int in a list of random int and verify if he matches with user answer
def match_number(random_list: [int]):
    the_number = random.choice(random_list)
    return the_number

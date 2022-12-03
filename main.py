from datetime import date
from importlib import import_module

from src.day import Day


def execute_day(day_number: int):
    """Load the selected day and executed the 2 parts and their test"""
    try:
        current_day_module = import_module(f"src.day{day_number:02}")
        if hasattr(current_day_module, f"Day{day_number:02}"):
            current_day_class: Day = (getattr(current_day_module, f"Day{day_number:02}"))()
            if current_day_class.test_1():
                print(current_day_class.part_1())
            else:
                print("Test 1 failure")
                print(current_day_class.get_test1_error())
            if current_day_class.test_2():
                print(current_day_class.part_2())
            else:
                print("Test 2 failure")
                print(current_day_class.get_test2_error())
        else:
            print("Error while trying to execute the current day:")
            print(f"No class Day{day_number:02} found")
    except ModuleNotFoundError as error:
        print("Error while importing the current day module:")
        print(error)
    except AttributeError as error:
        print("Error while executing the current day:")
        print(error)


def execute_current_day():
    """Load the current day of Advent of code and display the result of the two parts"""
    current_day = date.today().day
    execute_day(current_day)


if __name__ == '__main__':
    execute_current_day()
    # execute_day(1)

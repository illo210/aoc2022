from datetime import date
from importlib import import_module

from src.day import Day


def execute_current_day():
    """Load the current day of Advent of code and display the result of the two parts"""
    current_day = date.today().day
    try:
        current_day_module = import_module(f"src.day{current_day:02}")
        if hasattr(current_day_module, f"Day{current_day:02}"):
            current_day_class: Day = (getattr(current_day_module, f"Day{current_day:02}"))()
            print(current_day_class.part_1())
            print(current_day_class.part_2())
        else:
            print("Error while trying to execute the current day:")
            print(f"No class Day{current_day:02} found")
    except ModuleNotFoundError as error:
        print("Error while importing the current day module:")
        print(error)
    except AttributeError as error:
        print("Error while executing the current day:")
        print(error)


if __name__ == '__main__':
    execute_current_day()

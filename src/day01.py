"""
Advent of code 2022 Day 01.

For more information on the problem see https://adventofcode.com/2022/day/1.
"""
from typing import List, Optional

from src.day import Day


class Day01(Day):
    """
    Class representing the resolution of Advent of code 2022 Day 01.
    """

    """
    Calories of a snack as described in Advent of code 2022 Day 01.
    """
    Calories = int

    """
    Inventory of an elf as described in Advent of code 2022 Day 01.
    An inventory is composed of a list of number representing the calories of the snack possessed by the elf.
    """
    Inventory = List[Calories]

    def __init__(self):
        self.input = self._parse_empty_line_separated_input(lambda line: int(line))
        self.test_input = self._parse_empty_line_separated_input(lambda line: int(line), test=True)

    def _get_test_1_result(self) -> int:
        """
        Return the expected result of the part 1 for the test file.

        :return: the expected result of the part 1 for the test file.
        """
        return 24000

    def _get_test_2_result(self) -> int:
        """
        Return the expected result of the part 2 for the test file.

        :return: the expected result of the part 2 for the test file.
        """
        return 45000

    def _get_day(self) -> int:
        """
        Return the day this class is the implementation of the solution for.

        :return: the day this class is the implementation of the solution for.
        """
        return 1

    @staticmethod
    def _get_max_inventories(elves_inventories: List[Inventory],
                             number_of_maximum: Optional[int] = 1) -> int:
        """
        Calculate the sum of the number of calories in the inventory of `number_of_maximum` elves with the maximum
        calories.
        The objective of the Advent of code 2022 Day 01 is actually to calculate how many calories there is in the
        inventory of a variable number of elves(1 for part 1 and 3 for part 2). Moreover, these elves must be the ones
        carrying the most calories of the group.

        :param number_of_maximum: The number of elves to base the calculations on.
            This value of this parameter is the difference between part 1 and part 2
        :return: A number corresponding to the sum of all the calories in the inventory `number_of_maximum` elves with
        the maximum calories.
        """
        # First we add each number of calories in the inventory of the elves.
        summed_inventories = [sum(elf_inventory) for elf_inventory in elves_inventories]
        # Then we sorted by ordering the inventory with the most of the calories in front.
        total_calories_numbers = sorted(summed_inventories, reverse=True)
        # And finally we return the sum of the `number_of_maximum` inventories with the most calories.
        return sum(total_calories_numbers[:number_of_maximum])

    def part_1(self, elves_inventories: Optional[List[Inventory]] = None) -> int:
        """
        First part of Advent of code 2022 Day 01.

        :return: the answer for the first part.
        """
        elves_inventories = elves_inventories if elves_inventories is not None else self.input
        return self._get_max_inventories(elves_inventories, 1)

    def part_2(self, elves_inventories: Optional[List[Inventory]] = None) -> int:
        """
        Second part of Advent of code 2022 Day 01.

        :return: the answer for the second part.
        """
        elves_inventories = elves_inventories if elves_inventories is not None else self.input
        return self._get_max_inventories(elves_inventories, 3)

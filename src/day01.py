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

    elves_inventories: List[Inventory]

    def __init__(self):
        self.elves_inventories = self._parse_empty_line_separated_input(lambda line: int(line))

    def _get_day(self) -> int:
        return 1

    def _parse_input(self) -> List[Inventory]:
        """
        Parse the input of Advent of code 2022 Day 01.

        The input of this day is composed of a series of lines either empty or containing one number.
        Each group of numbers separated by an empty line represent the inventory of one elf.
        Each number represent the number of calories of a snack inside the elf inventory.

        :return: The list of the inventories of each elf.
        """
        with open(self._get_input_name()) as input_file:
            elf_inventories = [[]]
            for line in input_file:
                if len(line) > 1:
                    elf_inventories[-1].append(int(line))
                else:
                    elf_inventories.append([])
        return elf_inventories

    def _get_max_inventories(self, number_of_maximum: Optional[int] = 1) -> int:
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
        summed_inventories = [sum(elf_inventory) for elf_inventory in self.elves_inventories]
        # Then we sorted by ordering the inventory with the most of the calories in front.
        total_calories_numbers = sorted(summed_inventories, reverse=True)
        # And finally we return the sum of the `number_of_maximum` inventories with the most calories.
        return sum(total_calories_numbers[:number_of_maximum])

    def part_1(self) -> int:
        """
        First part of Advent of code 2022 Day 01.

        :return: the answer for the first part.
        """
        return self._get_max_inventories(1)

    def part_2(self) -> int:
        """
        Second part of Advent of code 2022 Day 01.

        :return: the answer for the second part.
        """
        return self._get_max_inventories(3)

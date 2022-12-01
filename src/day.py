"""
Implementation of the base class Day

For more information on the Advent of code see https://adventofcode.com/2022/.
"""
from typing import List, Any, TypeVar, Optional, Callable

T = TypeVar('T')


class Day:
    """
    Base class for the classes representing the resolution of Advent of code 2022.

    It contains utility functions which can be used in multiple days.
    It also provides a framework for the deriving classes of function to implement.
    """

    def _get_day(self) -> int:
        raise NotImplementedError

    def _parse_empty_line_separated_input(self, convert_line: Optional[Callable[[str], T]] = None) -> List[List[T]]:
        """
        Parse an input file composed of group of line with values separated by empty lines.
        An optional `convert_line` function can be passed. If given this function will be called on each line of
        value and the return will be stocked in the parsed input instead of the line.

        :return: A list of group of values.
        """
        with open(self._get_input_name()) as input_file:
            parsed_input = [[]]
            for line in input_file:
                # if the line isn't composed of only a return to line.
                if len(line) > 1:
                    parsed_input[-1].append(line if convert_line is None else convert_line(line))
                else:
                    # else we parse the next inputs as a separated group
                    parsed_input.append([])
                pass
        return parsed_input

    def _get_input_name(self) -> str:
        """
        Return the name of the input file for the current day.

        :return: the name of the input file for the current day.
        """
        return f'inputs/day{int(self._get_day()):02}/input.txt'

    def part_1(self) -> int:
        """
        First part of Advent of code 2022.

        :return: the answer for the first part.
        """
        raise NotImplementedError

    def part_2(self) -> int:
        """
        Second part of Advent of code 2022.

        :return: the answer for the second part.
        """
        raise NotImplementedError

"""
Implementation of the base class Day

For more information on the Advent of code see https://adventofcode.com/2022/.
"""
from typing import List, TypeVar, Optional, Callable, Union

T = TypeVar('T')
Input = TypeVar('Input')


class Day:
    """
    Base class for the classes representing the resolution of Advent of code 2022.

    It contains utility functions which can be used in multiple days.
    It also provides a framework for the deriving classes of function to implement.
    """

    """
    Input of the current day.
    """
    day_input = None
    """
    Input used in the tests.
    """
    test_input = None
    """
    Outputs of the tests. Filled after execution.
    """
    _test_output: List[Union[int, None]] = [None, None]

    def _get_day(self) -> int:
        """
        Return the day this class is the implementation of the solution for.

        :return: the day this class is the implementation of the solution for.
        """
        raise NotImplementedError

    def _parse_empty_line_separated_input(self,
                                          convert_line: Optional[Callable[[str], T]] = None,
                                          test: Optional[bool] = False) -> List[List[T]]:
        """
        Parse an input file composed of group of line with values separated by empty lines.

        :param convert_line: If given this function will be called on each line of value and the returned value
            will be stocked in the parsed input instead of the line.
        :return: A list of group of values.
        """
        file_name = self._get_input_name() if test is False else self._get_test_input_name()
        with open(file_name) as input_file:
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

    def _get_test_input_name(self) -> str:
        """
        Return the name of the input file for the current day.

        :return: the name of the input file for the current day.
        """
        return f'inputs/day{int(self._get_day()):02}/test.txt'

    def _get_test_1_result(self) -> int:
        """
        Return the expected result of the part 1 for the test file.

        :return: the expected result of the part 1 for the test file.
        """
        raise NotImplementedError

    def _get_test_2_result(self) -> int:
        """
        Return the expected result of the part 2 for the test file.

        :return: the expected result of the part 2 for the test file.
        """
        raise NotImplementedError

    def test_1(self) -> bool:
        """
        Test the part 1 against the expected output for the test file.
        In case of failure, use `get_test1_error` in order to get the error message.

        :return: a boolean indicated if the test was successful or not.
        """
        self._test_output[0] = self.part_1(self.test_input)
        return self._test_output[0] == self._get_test_1_result()

    def get_test1_error(self) -> str:
        """
        Return a string explaining the error for the test of the part 1

        :return: a string explaining the error for the test of the part 1
        """
        return f"Expected output: {self._get_test_1_result()}, but got {self._test_output[0]}"

    def test_2(self) -> bool:
        """
        Test the part 2 against the expected output for the test file.
        In case of failure, use `get_test2_error` in order to get the error message.

        :return: a boolean indicated if the test was successful or not.
        """
        self._test_output[1] = self.part_2(self.test_input)
        return self._test_output[1] == self._get_test_2_result()

    def get_test2_error(self) -> str:
        """
        Return a string explaining the error for the test of the part 2

        :return: a string explaining the error for the test of the part 2
        """
        return f"Expected output: {self._get_test_2_result()}, but got {self._test_output[1]}"

    def part_1(self, day_input: Optional[Input] = None) -> int:
        """
        First part of Advent of code 2022.

        :return: the answer for the first part.
        """
        raise NotImplementedError

    def part_2(self, day_input: Optional[Input] = None) -> int:
        """
        Second part of Advent of code 2022.

        :return: the answer for the second part.
        """
        raise NotImplementedError

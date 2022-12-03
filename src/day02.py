"""
Advent of code 2022 Day 02.

For more information on the problem see https://adventofcode.com/2022/day/2.
"""
from __future__ import annotations

import enum
from typing import List, Optional

from src.day import Day


class _MOVE(enum.IntEnum):
    """
    Class representing a move in the game Rock Paper Scissor during the day 02 of Advent of code.
    """
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    def get_points(self) -> int:
        """
        Return the number of point gained for playing that move.

        :return: The number of point gained for playing that move.
        """
        return self.value


class _MATCH_OUTPUT(enum.IntEnum):
    """
    Class representing the outcome of a game of Rock Paper Scissor during the day 02 of Advent of code.
    It is possible to use an arithmetic solution in order to get the result of `get_matching_move` and
    `get_match_output` functions, but due to the low number of moves, we used a conditional solution for clarity.
    """
    LOOSE = 0
    DRAW = 3
    VICTORY = 6

    def get_points(self) -> int:
        """
        Return the number of point gained for playing that match.

        :return: The number of point gained for playing that match.
        """
        return self.value

    def get_matching_move(self, opponent_move: _MOVE) -> _MOVE:
        """
        Get the move you need to play in order to get the current match output.

        :param opponent_move: The move your opponent played during this match.
        :return: The move you need to play in order to get the current match output.
        """
        if self is _MATCH_OUTPUT.LOOSE:
            if opponent_move is _MOVE.ROCK:
                matching_move = _MOVE.SCISSOR
            elif opponent_move is _MOVE.PAPER:
                matching_move = _MOVE.ROCK
            else:
                matching_move = _MOVE.PAPER
        elif self is _MATCH_OUTPUT.DRAW:
            matching_move = opponent_move
        else:
            if opponent_move is _MOVE.ROCK:
                matching_move = _MOVE.PAPER
            elif opponent_move is _MOVE.PAPER:
                matching_move = _MOVE.SCISSOR
            else:
                matching_move = _MOVE.ROCK
        return matching_move

    @staticmethod
    def get_match_output(self_move: _MOVE, opponent_move: _MOVE) -> _MATCH_OUTPUT:
        """
        Get the output of a match, using your move and the move of your opponent.

        :param self_move: The move you played during that match
        :param opponent_move: The move your opponent played
        :return: The output of the match played.
        """
        if self_move is _MOVE.ROCK:
            if opponent_move is _MOVE.ROCK:
                match_output = _MATCH_OUTPUT.DRAW
            elif opponent_move is _MOVE.PAPER:
                match_output = _MATCH_OUTPUT.LOOSE
            else:
                match_output = _MATCH_OUTPUT.VICTORY
        elif self_move is _MOVE.PAPER:
            if opponent_move is _MOVE.ROCK:
                match_output = _MATCH_OUTPUT.VICTORY
            elif opponent_move is _MOVE.PAPER:
                match_output = _MATCH_OUTPUT.DRAW
            else:
                match_output = _MATCH_OUTPUT.LOOSE
        else:
            if opponent_move is _MOVE.ROCK:
                match_output = _MATCH_OUTPUT.LOOSE
            elif opponent_move is _MOVE.PAPER:
                match_output = _MATCH_OUTPUT.VICTORY
            else:
                match_output = _MATCH_OUTPUT.DRAW
        return match_output


class Day02(Day):
    """
    Class representing the resolution of Advent of code 2022 Day 02.
    """

    input_type = List[List[str]]

    def __init__(self):
        self.input = self._parse_simple_list_input(convert_line=lambda line: line.split(" "))
        self.test_input = self._parse_simple_list_input(convert_line=lambda line: line.split(" "), test=True)

    def _get_day(self) -> int:
        """
        Return the day this class is the implementation of the solution for.

        :return: the day this class is the implementation of the solution for.
        """
        return 2

    def _get_test_1_result(self) -> int:
        """
        Return the expected result of the part 1 for the test file.

        :return: the expected result of the part 1 for the test file.
        """
        return 15

    def _get_test_2_result(self) -> int:
        """
        Return the expected result of the part 2 for the test file.

        :return: the expected result of the part 2 for the test file.
        """
        return 12

    def part_1(self, day_input: Optional[input_type] = None) -> int:
        """
        First part of Advent of code 2022 Day 02.

        :return: the answer for the first part.
        """
        day_input = self.input if day_input is None else day_input
        points = 0
        elf_move_input = {
            "A": _MOVE.ROCK,
            "B": _MOVE.PAPER,
            "C": _MOVE.SCISSOR,
        }
        self_move_input = {
            "X": _MOVE.ROCK,
            "Y": _MOVE.PAPER,
            "Z": _MOVE.SCISSOR,
        }
        for line in day_input:
            opponent_move = elf_move_input[line[0]]
            self_move = self_move_input[line[1]]
            match_output = _MATCH_OUTPUT.get_match_output(self_move, opponent_move)
            points += self_move.get_points() + match_output.get_points()
        return points

    def part_2(self, day_input: Optional[input_type] = None) -> int:
        """
        Second part of Advent of code 2022 Day 02.

        :return: the answer for the second part.
        """
        day_input = self.input if day_input is None else day_input
        points = 0
        elf_move_input = {
            "A": _MOVE.ROCK,
            "B": _MOVE.PAPER,
            "C": _MOVE.SCISSOR,
        }
        match_output_input = {
            "X": _MATCH_OUTPUT.LOOSE,
            "Y": _MATCH_OUTPUT.DRAW,
            "Z": _MATCH_OUTPUT.VICTORY
        }
        for line in day_input:
            opponent_move = elf_move_input[line[0]]
            match_output = match_output_input[line[1]]
            self_move = match_output.get_matching_move(opponent_move)
            points += self_move.get_points() + match_output.get_points()
        return points

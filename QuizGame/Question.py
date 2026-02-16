"""
Question class for State Capitals Quiz
Author: Kevin Vo, Anthony Marcos
Date: 02/16/2026
Description: Represents a single state capital question.
"""

import random


class Question:
    """Represents a state capital quiz question"""

    def __init__(self, states):
        """
        Initialize a Question object.

        :param states: dictionary of state:capital pairs
        """
        # Choose random state and capital
        self._state, self._correct_capital = random.choice(list(states.items()))

        # Possible choices (can change size later without breaking code)
        self._possible_choices = ['A', 'B', 'C', 'D']

        # Build selections list
        self._selections = [self._correct_capital]

        # Get incorrect capitals
        incorrect_capitals = list(states.values())
        incorrect_capitals.remove(self._correct_capital)

        while len(self._selections) < len(self._possible_choices):
            choice = random.choice(incorrect_capitals)
            if choice not in self._selections:
                self._selections.append(choice)

        # Shuffle selections
        random.shuffle(self._selections)

        # Determine correct answer letter
        correct_index = self._selections.index(self._correct_capital)
        self._answer = self._possible_choices[correct_index]

    @property
    def possible_choices(self):
        """Return list of possible choice letters"""
        return self._possible_choices

    def check_correct(self, selection):
        """Check if user selection is correct
        """
        return selection == self._answer

    def correct_response(self):
        """Return correct response message"""
        return f"Correct! {self._correct_capital} is the capital of {self._state}."

    def incorrect_response(self):
        """Return incorrect response message"""
        return f"Your answer was incorrect! The correct answer was: {self._answer}. {self._correct_capital}."

    def __str__(self):
        """Return formatted question string"""
        question_str = f"The capital of {self._state} is:\n"
        for letter, capital in zip(self._possible_choices, self._selections):
            question_str += f"   {letter}. {capital}   "
        return question_str.strip()

"""
State Capitals Quiz
Author: Kevin Vo, Anthony Marcos
Date: 02/16/2026
Description: Quiz program that tests user on U.S. state capitals
"""

from question import Question


def read_file_to_dictionary(filename):
    """Read state capital pairs from a file into dictionary"""
    states = {}
    with open(filename, 'r') as file:
        for line in file:
            state, capital = line.strip().split(',')
            states[state] = capital
    return states


def get_user_choice(valid_options):
    """Prompt user until valid choice is entered"""
    while True:
        choice = input("Enter choice: ").upper()
        if choice in valid_options:
            return choice
        print(f"Invalid input. Enter {'-'.join(valid_options)}.")


def ask_question(number, states):
    """Ask a quiz question"""
    question = Question(states)
    print(f"\n{number}. {question}")

    user_choice = get_user_choice(question.possible_choices)

    if question.check_correct(user_choice):
        print(question.correct_response())
        return 1
    else:
        print(question.incorrect_response())
        return 0


def main():
    """Main program loop"""
    print("- State Capitals Quiz -")

    states = read_file_to_dictionary("statecapitals.txt")
    points = 0

    for i in range(1, 11):
        points += ask_question(i, states)

    print(f"\nEnd of test. You got {points} correct.")


main()

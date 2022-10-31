# quiz.py

import pathlib
import random
from string import ascii_lowercase
from this import d
import tomli as tomllib
import termcolor as tc
from termcolor import colored

#COLOURED CORRECT ANSWER:
wans= colored("⭐️Correct Answer⭐️!", "green", attrs=['reverse'])

NUM_QUESTIONS_PER_QUIZ = 9
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"

#FUNCTION THAT RUNS THE ENTIRE QUIZ
def run_quiz():
    questions = prepare_questions(
        QUESTIONS_PATH, num_questions=NUM_QUESTIONS_PER_QUIZ
    ) #USED TO ACCESS THE OTHER FILE

    num_correct = 0
    for num, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question)

    print(f"\nYou got {num_correct} correct out of {num} questions")
    #TO DISPLAY USER SCORE

#PREREQUISITES
def prepare_questions(path, num_questions):
    questions = tomllib.loads(path.read_text())["questions"]
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, k=num_questions)

#FUNCTION TO ASK USER QUESTIONS
def ask_question(question):
    correct_answer = question["answer"]
    alternatives = [question["answer"]] + question["alternatives"]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question["question"], ordered_alternatives)
    if answer == correct_answer:
        
        print(wans)
        return 1
    else:
        cans= colored(f"The answer is {correct_answer!r}, not {answer!r}", "red", attrs=['reverse'])
        print(cans)
        return 0

#FUNCTION TO GET USERS RESPONSE
def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]


if __name__ == "__main__":
    run_quiz()

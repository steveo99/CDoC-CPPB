"""
100 Days of Code, Day 17, Lesson 120
Quiz Project
"""

import random
from d017q.question_model import Question
from d017q.data import question_data, get_open_trivia_db_data
from d017q.quiz_brain import QuizBrain


def get_question_data():
    """
    load question_data into a list of Question objects
    """
    question_bank = []
    questions = []
    ans = input(
        "Use the 1) course questions, or the 2) Open Trivia DB questions? 1/2: "
    )
    if ans == "1":
        questions = question_data
        question_key = "text"
        answer_key = "answer"
    elif ans == "2":
        questions = get_open_trivia_db_data()
        question_key = "question"
        answer_key = "correct_answer"
    else:
        print("invalid response")
        return
    # print(questions)
    for question in questions:
        question_bank.append(Question(question[question_key], question[answer_key]))
    random.shuffle(question_bank)
    return question_bank


def main():
    """
    Code for Day 17 Lesson 120
    Quiz Project
    """
    question_bank = get_question_data()
    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()
    quiz.final_score()


if __name__ == "__main__":
    main()

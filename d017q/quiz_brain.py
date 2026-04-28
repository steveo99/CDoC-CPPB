"""
QuizBrain class
"""


class QuizBrain:
    """
    QuizBrain class for Quiz Project
    """

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        """
        prompt for the next question
        """
        question = self.question_list[self.question_number]
        self.question_number += 1
        prompt = f"Q.{self.question_number}. {question.text} (True/False): "
        ans = self.get_valid_answer(prompt)
        self.check_answer(ans, question.answer)

    def get_valid_answer(self, prompt):
        """
        display the prompt, get user input
        allow the user to input True, t or y for True, False, f or n for False
        return the valid answer
        """
        ans = ""
        while ans not in ["True", "False"]:
            ans = input(prompt).lower()
            if ans in [
                "true",
                "t",
                "y",
            ]:
                ans = "True"
            elif ans in [
                "false",
                "f",
                "n",
            ]:
                ans = "False"
        return ans

    def still_has_questions(self):
        """
        are there still questions left to ask
        """
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """
        check if the answer is correct, increment score if correct
        """

        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")

    def final_score(self):
        """
        print they have finished the quiz.
        show the final score.
        """
        print("You've completed the quiz.")
        print(f"Your final score was: {self.score}/{self.question_number}.\n")

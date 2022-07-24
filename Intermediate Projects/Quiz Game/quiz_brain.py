class QuizBrain:
    def __init__(self, question_list):  # question_bank will be passed into this
        self.question_list = question_list  # list of all the questions with their answers
        self.question_number = 0  # current question number
        self.score = 0  # current user score

    def still_has_questions(self):
        return self.question_number < len(self.question_list)  # while the current question number has not reached the last question, return True

    def next_question(self):
        current_question = self.question_list[self.question_number]  # gets the current question similar to question_bank[0]
        self.question_number += 1  # increment the question number so that next time it runs it will be on a different question
        user_input = input(f'Q.{self.question_number}: {current_question.text} (True/False)?: ')  # get user input
        self.check_answer(user_input,current_question.answer)  # pass through user input and correct answer

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():  # if the user guessed correctly
            print("You got it right!")
            self.score += 1  # add one to the current score
        else:
            print("That's wrong")
            print(f'The correct answer was: {correct_answer}')  # show correct answer
        print(f'Your current score is: {self.score}/{self.question_number}')  # show how many they got right out of current question number they are on, such as 3/5
        print('\n')
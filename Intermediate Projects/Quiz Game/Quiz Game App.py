from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []  # Will hold all the instances of different questions
for questions in question_data:  # for each question in the dictionary
    question = questions['question']
    answer = questions['correct_answer']

    qd = Question(question, answer)  # create an instance using the information

    question_bank.append(qd)  # add it to the other list of different instances

quiz = QuizBrain(question_bank)  # pass through the list of questions to the QuizBrain class

while quiz.still_has_questions():  # while the function has not reached the last question
    quiz.next_question()  # ask the next question

# when quiz has ended
print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")  # call the class variables for score and question number to show final score

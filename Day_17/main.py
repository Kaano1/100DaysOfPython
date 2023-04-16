from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for q in question_data:
    question_text = q["question"]
    quesiton_answer = q["correct_answer"]
    question_bank.append(Question(question_text, quesiton_answer))

game = QuizBrain(question_bank)
game.next_question()
print("You completed the quiz")
print(f"Your final score was: {game.score}/{len(game.question_list)}")

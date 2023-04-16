class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def next_question(self):
        index = self.question_number
        while index < len(self.question_list):
            ask = self.question_list[index]
            index += 1
            answer = input(f"Q.{index} {ask.text} (True or False): ").lower()
            if answer != ask.answer.lower():
                print("That's Wrong.")
            else:
                self.score += 1
                print("You got it!")
            print(f"Your currently score is {self.score}/{index}\n")

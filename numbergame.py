import random
import time


class NumbersGame:
    def __init__(self):
        self.x = 1
        self.y = 100

        self.answer = random.randint(self.x, self.y)
        self.guess = ""

        print("Guess the number between 1 and 100. If you guess the number you LOSE!")
        time.sleep(1)
        self.guess_number()

    def guess_number(self):
        self.guess = int(input("Enter a number between " + str(self.x) + " and " + str(self.y) + ": "))
        self.check_answer()

    def check_answer(self):
        if self.guess == self.answer:
            print("YOU LOSE!")
            time.sleep(2)
            NumbersGame()
        elif self.guess < self.answer:
            self.x = self.guess
            print(self.x)
            print(self.y)
            self.guess_number()

        elif self.guess > self.answer:
            self.y = self.guess
            print(self.x)
            print(self.y)
            self.guess_number()


NumbersGame()

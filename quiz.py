import datetime
import random


from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        # generate 10 random questions with numbers from 1-10
        quiz_item1 = Add(4, 4)
        quiz_item2 = Multiply(2, 3)
        # use a range to generate number
        for _ in range(10):
            # choose add or multiply
            # choose a random digit to use as arguments 
        # add these questions into self.questions
        self.questions.append(quiz_item1.text)
        self.questions.append(quiz_item2.text)

    def take_quiz(self):
        # log the start time
            # run datetime.datetime.now()
        # ask all of the questions -> ask func
        # log if they got the question right -> output to a text file or on the console
        # log the end time
        # show a summary -> summary func
        pass

    def ask(self, question):
        # log the start time
        # capture the answer -> input func
        # check the answer
        # log the end time
        # if the answer's right, send back True
        # otherwise, send back False
        # send back the elapsed time, too
        pass

    def summary(self):
        # print how many you got right and the total # of questions
        # print the total time for the quiz: 30 seconds
        pass
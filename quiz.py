import datetime
import random


from questions import Add, Multiply


class Quiz:
    questions = []
    answers = []

    def __init__(self):
        question_types = (Add, Multiply)  # this tuple is a sequence!
        # generate 10 random questions with numbers from 1-10
        for _ in range(10):
            num1 = random.randint(1,10)
            num2 = random.randint(1,10)
            # random.choice is used for sequences AKA seq
            question = random.choice(question_types)(num1, num2)
            self.questions.append(question)

    def take_quiz(self):
        # log the start time
        start_time = datetime.datetime.now()

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

    def total_correct(self):
        total = 0
        for answer in self.answers:
            # The first index of `answer` is a boolean telling us if they got the question right or wrong.
            # I think this is also the answer.answer attribute 
            if answer[0]:
                total += 1
        return total  

    def summary(self):
        # print how many you got right and the total # of questions
        print("You got {} out of {} right".format(
            self.total_correct(), len(self.questions)
        ))
        # compute a timedelta and use its seconds
        print("It took you {} seconds total.".format(
            (self.end_time-self.start_time).seconds
        ))
        pass
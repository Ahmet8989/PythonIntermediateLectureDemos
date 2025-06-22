class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {(self.questionIndex) + 1}..: { question.text } ")

        for choice in question.choices:
            print(f"- " + choice)

        answer = input(f"Answer..: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if (question.checkAnswer(answer)):
            self.score += 1

        self.questionIndex += 1

    def loadQuestion(self):
        if(len(self.questions) == self.questionIndex):
            self.showScore()
        else:
            self.displayQuestion()


    def showScore(self):
        print(f"Score..: {self.score}")

q1 = Question("What is the best programming language?", 
              ["C#", "Python", "Javascript", "Java"], 
              "Python")

q2 = Question("What is the most popular programming language?", 
              ["C#", "Python", "Javascript", "Java"], 
              "Python")

q3 = Question("What is the best income bringer programming language?", 
              ["C#", "Python", "Javascript", "Java"], 
              "Python")

questions = [q1, q2, q3]

quiz = Quiz(questions)
quiz.displayQuestion()
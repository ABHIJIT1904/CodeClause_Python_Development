### Speed Typing Test in python ### 



import time
import threading



class tester:
    def __init__(self, paragraph):
        self.correctWords = []
        self.incorrectWords = {}
        self.typedWords = []
        self.totalWords = []
        self.input = None
        self.paragraph = paragraph
        self.accuracy = 0
        self.time = 0
        self.wordPermin = 0
        self.run()



    def clock(self):
        while len(self.typedWords) == 0:
            self.time += 1
            time.sleep(1)

    def run(self):
        threading.Thread(target=self.clock).start()
        threading.Thread(target=self.testSpeed).start()

    def testSpeed(self):
        print('\n\n'+self.paragraph+'\n\n')
        self.input = str(input('\t\n'+'Type The Above Sentence By Which You Can Find Your Speed As Well As Spelling Mistakes. \n\n'))
        self.totalWords = self.paragraph.split(' ')
        self.typedWords = self.input.split(' ') 

        try:
            for i in range(len(self.typedWords)):
                if(self.typedWords[i] == self.totalWords[i]):
                    self.correctWords.append(self.typedWords[i])
                else:
                    self.incorrectWords.update({self.totalWords[i] : self.typedWords[i]})

        except Exception as e:
            print(e)


        self.accuracy = len(self.correctWords)/len(self.typedWords) * 100
        self.wordPerMin = len(self.typedWords) / (self.time/60)

        print('\n\nResult :--')
        print(f'Accuracy: -- {self.accuracy}')
        print(f'Word Per Minute :-- {self.wordPerMin}')
        print(f'Incorrect Words :-- {self.incorrectWords}')

Mytester = tester("You know you're a programmer when you spend a whole day to find the problem in the code, and then fix it with one line of code.")



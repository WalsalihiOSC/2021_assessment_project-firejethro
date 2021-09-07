import random
from tkinter import *

# Global Functions

root = Tk()
root.title("Math Game")
root.geometry("400x300")

# Page Functions
class App:
# Name Page
    def __init__(self):
        self.frame = Frame(root)
        self.frame.grid()

        # Creating and placing Labels
        title = Label(self.frame, text = "Math Game").grid(row = 0, column = 1, pady = 20)
        namelabel = Label(self.frame, text = "Name:").grid(row = 1, column = 0)
        self.nameentry = Entry(self.frame)
        self.nameentry.grid(row = 1, column = 1)
        startbutton = Button(self.frame, text = "Start", command = self.verify).grid(row = 2, column = 2)

    # Record name as variable and switch frame
    def verify(self):
        name = self.nameentry.get()
        self.frame.destroy()
        self.difficulty()


# Difficulty Page
    def difficulty(self):
        
        # Create new frame
        self.frame = Frame(root)
        self.frame.grid()

        # Setting starting variables for Change Difficulty Function Loop
        self.difficultyindex = 0
        print(F"Index Set to 0")
        self.difficulties = ["Easy", "Medium", "Hard"]

        # Creating and placing Labels
        title = Label(self.frame, text = "Select Difficulty").grid(row = 0, column = 1, pady = 20)
        clicktochange = Label(self.frame, text = "Click to Change").grid(row = 1, column = 1)
        self.difficultybutton = Button(self.frame, text = "Easy", command = self.changedifficulty)
        self.difficultybutton.grid(row = 2, column = 1)
        playbutton = Button(self.frame, text = "Play", command = self.play).grid(row = 2, column = 2)

    # Change Difficulty Function
    def changedifficulty(self):
        print(F"Index Changed to {self.difficultyindex}")
        if self.difficultyindex <= 1:
            self.difficultyindex += 1
        else:
            self.difficultyindex = 0
        # Change difficulty button text 
        difficulty = self.difficulties[self.difficultyindex]
        self.difficultybutton.config(text = difficulty)
    
    def play(self):
        # Destroy frame
        self.frame.destroy()

        # Set ranges based on difficulty
        addsubmin = 0
        muldivmin = 0
        signmin = 0
        if self.difficultyindex == 0:
            self.addsubmax = 100
            self.signmax = 1
        elif self.difficultyindex == 0:
            self.addsubmax = 100
            self.muldivmax = 12
            self.signmax = 3
        else:
            self.addsubmax = 1000
            self.muldivmax = 100
            self.signmax = 3

        # Initialize Gameplay Function
        self.gameplay()

# Gameplay Setup
    def gameplay(self):
        
        self.questionindex = 1

        # Create new frame
        self.frame = Frame(root)
        self.frame.grid()

        # Generate equation
        # Generate sign
        # Random integer, 0 = Addition, 1 = Subtraction, 2 = Multiplication, 4 = Division
        signindex = random.randint(0, self.signmax)

        # If Addition/Subtraction
        if signindex <= 1:
            numberone = random.randint(1, self.addsubmax)
            numbertwo = random.randint(1, self.addsubmax)
            if signindex == 1:
                sign = "+"
                self.answer = numberone + numbertwo
            else:
                sign = "-"
                self.answer = numberone - numbertwo
        
        # If Multiplication/Division
        else:
            numberone = random.randint(1, self.muldivmax)
            numbertwo = random.randint(1, self.muldivmax)
            if signindex == 1:
                sign = "×"
                self.answer = numberone * numbertwo
            else:
                sign = "÷"
                product = numberone * numbertwo
                self.answer = product / numberone

        # Create equation strings
        self.equation = F"{numberone} {sign} {numbertwo}"
        self.questionnumberlabel = F"Question {self.questionindex} of 10"
        
        # Gameplay Page Setup
        self.questionnumber = Label(self.frame, text = self.questionnumberlabel).grid(row = 0, column = 1, pady = 20)
        equationlabel = Label(self.frame, text = self.equation).grid(row = 2, column = 1)
        self.response = Entry(self.frame)
        self.response.grid(row = 3, column = 1)
        Button(self.frame, text = "Submit", command = self.submit).grid(row = 3, column = 2)

    # Record response as variable and switch frame
    def submit(self):
        self.response = self.response.get()
        print(self.response)

    # Valid Integer Check function
    def numcheck(self, numtype, question, low, high, errormsg, valuemsg):
        while True:
            try:
                response = int(self.response)
                if low <= response and response <= high:
                    return response
                else:
                    print(errormsg)
            except ValueError:
                print(valuemsg)

    # Check if answer is correct 
        
# Scoreboard Page

'''
# Data Encapsulation Class
class Player:
    def __init__(self, name, highscore):
        name = self.name
        highscore = self.highscore
'''

App()
root.mainloop()
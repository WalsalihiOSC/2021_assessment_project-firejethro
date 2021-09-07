import random
from tkinter import *

root = Tk()
root.title("Math Game")
root.geometry("400x300")

# Page Functions
class App:

    # Close Frame Function
    def closeframe(self):
        self.frame.destroy()
    
    # Contructor + Name Page
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
        self.closeframe()
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
        
        if self.difficultyindex <= 1:
            self.difficultyindex += 1
        else:
            self.difficultyindex = 0
        print(F"Index Changed to {self.difficultyindex}")

        # Change difficulty button text 
        difficulty = self.difficulties[self.difficultyindex]
        self.difficultybutton.config(text = difficulty)
    
    def play(self):

        # Close frame
        self.closeframe()

        # Set variables
        self.questionindex = 1
        self.correctresponses = 0

        # Set ranges based on difficulty
        addsubmin = 0
        muldivmin = 0
        signmin = 0

        # Easy
        if self.difficultyindex == 0:
            self.addsubmax = 100
            self.signmax = 1

        # Medium
        elif self.difficultyindex == 1:
            self.addsubmax = 100
            self.muldivmax = 12
            self.signmax = 3

        # Hard
        else:
            self.addsubmax = 1000
            self.muldivmax = 100
            self.signmax = 3

        # Initialize Gameplay Function
        self.generatequestion()

# Generate question
    def generatequestion(self):
        
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
            if signindex == 3:
                sign = "×"
                self.answer = numberone * numbertwo
            else:
                sign = "÷"

                # Logic to make sure answer is a whole number
                numberone = numberone * numbertwo
                self.answer = numberone / numbertwo

        # Create equation strings
        self.equation = F"{numberone} {sign} {numbertwo}"
        self.questionnumberlabel = F"Question {self.questionindex} of 10"
        
        # Gameplay Displayed Page Setup
        Label(self.frame, text = self.questionnumberlabel).grid(row = 0, column = 1, pady = 20)
        Label(self.frame, text = self.equation, font = ("Arial", 50)).grid(row = 2, column = 1)
        self.responseentry = Entry(self.frame)
        self.responseentry.grid(row = 3, column = 1)
        Button(self.frame, text = "Submit", command = self.submit).grid(row = 3, column = 2)

    # Analyze response
    def submit(self):

        # Record response as integer variable
        self.response = self.responseentry.get()
        self.response = self.response.replace(" ", "")

        try:
            self.response = int(self.responseentry.get())
            self.markresponse()
            
        # If response is NOT a valid integer
        except ValueError:

            # Create error window
            errorwindow = Tk()

            # Close error window function
            def closewindow():
                errorwindow.destroy()

            # Create and place labels and button
            invalidresponselabel = F"{self.response} is not a valid number."
            Label(errorwindow, text = invalidresponselabel).grid(row = 0, column = 1)
            Button(errorwindow, text = "Retry", command = closewindow).grid(row = 1, column = 1)

            # Initialize Tkinter error window
            errorwindow.mainloop

            print("Invalid")


    def markresponse(self):
        # If response IS a valid integer

        # Close frame, create Correct/Incorrect frame
        self.closeframe()
        self.frame = Frame(root)
        self.frame.grid()

        # Create and place label based on if answer correct or incorrect
        if self.response == self.answer:
            print("Correct")
            Label(self.frame, text = "Correct").grid(row = 0, column = 1)
            self.correctresponses += 1
        else:
            print("Incorrect")
            Label(self.frame, text = "Incorrect").grid(row = 1, column = 1)

        # Add to question index
        self.questionindex += 1        

        # Place current score label
        currentscorelabel = F"{self.correctresponses} of {self.questionindex}"
        Label(self.frame, text = currentscorelabel)
        Button(self.frame, text = "Next", command = self.nextquestion).grid(row = 2, column = 1)
        
    def nextquestion(self):
        self.closeframe()
        if self.questionindex <= 10:
            self.generatequestion()
        else:
            self.closeframe()
            print("Round Complete")

# Scoreboard Page

'''
# Data Encapsulation Class
class Player:
    def __init__(self, name, highscore):
        name = self.name
        highscore = self.highscore
'''

# Initialize class and Tkinter root window
App()
root.mainloop()
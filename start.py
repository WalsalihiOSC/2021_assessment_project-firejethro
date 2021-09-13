import random
from player import *
from tkinter import *

root = Tk()
root.title("Math Game")
root.geometry("840x480")

# Page Functions
class App:

    # Create new frame function
    def createnewframe(self):
        self.frame = Frame(root)
        self.frame.place(width = 840, height = 480, relx = 0.5, rely = 0.5, anchor = CENTER)

    # Close Frame Function
    def closeframe(self):
        self.frame.destroy()

    # Title Label function
    def titlelabel(self, titletext):
        self.title = Label(self.frame, text = titletext, font = ('Comic Sans MS', 50), fg = '#FFFFFF', bg = '#4285F4')
        self.title.place(width = 840, relx = 0.5, rely = 0, anchor = N)

    # Contructor + Name Page
    def __init__(self):
        self.createnewframe()

        # Creating and placing Labels
        self.titlelabel("Math Game")
        
        namelabel = Label(self.frame, text = "Name:", font = ('Comic Sans MS', 30), fg = '#414141')
        namelabel.place(relx = 0.25, rely = 0.5, anchor = CENTER)

        self.nameentry = Entry(self.frame, font = ('Comic Sans MS', 30))
        self.nameentry.place(width = 260, height = 80, relx = 0.5, rely = 0.5, anchor = CENTER)

        nextbutton = Button(self.frame, text = "Next", command = self.verify, font = ('Comic Sans MS', 30), fg = '#FFFFFF', bg = '#4285F4', borderwidth = 12)
        nextbutton.place(width = 180, height = 80, relx = 0.80, rely = 0.8, anchor = CENTER)

    # Record name as variable and switch frame
    def verify(self):
        self.name = self.nameentry.get()
        
        
        # If response field is EMPTY
        if self.name == "":

            # Create and place error text under entry box
            errorlabel = Label(self.frame, text = "Enter your name into the box above.", font = ('Comic Sans MS', 20), fg = '#FF0000')
            errorlabel.place(relx = 0.5, rely = 0.65, anchor = CENTER)

        # If name entered
        else:
            self.closeframe()
            self.difficulty()

# Difficulty Page
    def difficulty(self):
        
        # Create new frame
        self.createnewframe()

        # Setting starting variables for Change Difficulty Function Loop
        self.difficultyindex = 0
        print(F"Index Set to 0")
        self.difficulties = ["Easy", "Medium", "Hard"]

        # Creating and placing Labels
        self.titlelabel("Select Difficulty")

        clicktochange = Label(self.frame, text = "Click to Change", font = ('Comic Sans MS', 20))
        clicktochange.place(relx = 0.5, rely = 0.325, anchor = CENTER)

        self.difficultybutton = Button(self.frame, text = "Easy", command = self.changedifficulty, font = ('Comic Sans MS', 30), fg = '#FFFFFF', bg = '#4285F4', borderwidth = 12)
        self.difficultybutton.place(width = 260, height = 80, relx = 0.5, rely = 0.45, anchor = CENTER)
    

        startbutton = Button(self.frame, text = "Start", command = self.play, font = ('Comic Sans MS', 30), fg = '#FFFFFF', bg = '#1DD600', borderwidth = 12)
        startbutton.place(width = 170, height = 80, relx = 0.80, rely = 0.8, anchor = CENTER)

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
    
    # Start Game Function
    def play(self):

        # Close frame
        self.closeframe()

        # Set variables
        self.questionindex = 0
        print(F"Question Index set to {self.questionindex}")
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
        
        # Add to question index
        self.questionindex += 1
        print(F"Question Index changed to {self.questionindex}")
        
        # Create new frame
        self.createnewframe()

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
                self.answer = float(numberone + numbertwo)
            else:
                sign = "-"
                self.answer = float(numberone - numbertwo)
        
        # If Multiplication/Division
        else:
            numberone = random.randint(1, self.muldivmax)
            numbertwo = random.randint(1, self.muldivmax)
            if signindex == 3:
                sign = "×"
                self.answer = float(numberone * numbertwo)
            else:
                sign = "÷"

                # Logic to make sure answer is a whole number
                numberone = numberone * numbertwo
                self.answer = float(numberone / numbertwo)

        # Create equation strings
        self.equation = F"{numberone} {sign} {numbertwo}"
        self.questionindexlabel = F"Question {self.questionindex} of 10"
        
        # Gameplay Displayed Page Setup
        Label(self.frame, text = self.questionindexlabel).grid(row = 0, column = 1, pady = 20)
        Label(self.frame, text = self.equation, font = ("Arial", 50)).grid(row = 2, column = 1)
        self.responseentry = Entry(self.frame)
        self.responseentry.grid(row = 3, column = 1)
        Button(self.frame, text = "Submit", command = self.submit).grid(row = 3, column = 2)

    # Analyze response
    def submit(self):

        # Record response as variable
        self.response = self.responseentry.get()
        self.response = self.response.replace(" ", "")

        # Try if response is valid number
        try:
            self.response = float(self.responseentry.get())
            self.markresponse()

        # If response is NOT a valid number
        except ValueError:

            # Create error window
            errorwindow = Tk()

            # Close error window function
            def closewindow():
                errorwindow.destroy()

            # Create and place labels and button

            # If response field is EMPTY
            if self.response == "":
                invalidresponselabel = F"Enter a number into the answer field."

            # If invalid response entered
            else:
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
        self.createnewframe()

        # Create and place label based on if answer correct or incorrect
        if self.response == self.answer:
            print("Correct")
            Label(self.frame, text = "Correct").grid(row = 0, column = 1)
            self.correctresponses += 1
        else:
            print("Incorrect")
            Label(self.frame, text = "Incorrect").grid(row = 1, column = 1)       

        # Place current score label
        currentscorelabel = F"{self.correctresponses} of {self.questionindex}"
        Label(self.frame, text = currentscorelabel)
        Button(self.frame, text = "Next", command = self.nextquestion).grid(row = 2, column = 1)
        
    def nextquestion(self):
        self.closeframe()

        # If below question limit
        if self.questionindex < 1:
            self.generatequestion()

        # If question limit reached
        else:
            self.closeframe()

            # Create newplayer object in Player class
            newplayer = Player(self.name, self.correctresponses, self.questionindex)

            # Create new frame
            self.createnewframe()

            # Game over and final score labels
            Label(self.frame, text = "Game Over").grid(row = 0, column = 1)
            finalscorelabel = F"{self.correctresponses} of {self.questionindex} correct"
            Label(self.frame, text = finalscorelabel).grid(row = 0, column = 1)

            # Instance of player
            Player.displayprofile(newplayer)
            Player.saveprofile(newplayer)
            self.closeframe()
            self.scoreboard()

    # Scoreboard Page
    def scoreboard(self, previouspage):
        scoreboardwindow = Tk()
        print("Scoreboard initiate")
        Label(self.frame, text = "Scoreboard").grid(row = 0, column = 1)
        f = open("savedplayers.txt", "r")
        contents = (f.read())
        Label(self.frame, text = contents).grid(row = 0, column = 1)
        f.close()

# Initialize class and Tkinter root window
App()
root.resizable(False, False)
root.mainloop()
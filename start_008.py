import random
from player import *
from tkinter import *

root = Tk()
root.title("Math Game")
root.geometry("840x480")

# Color Palette
white = '#FFFFFF'
red = '#FF0000'
gray = '#414141'
green = '#1DD600'
blue = '#4285F4'

# Dim Shades
dimred = '#B52E2E'
dimblue = '#48629C'
dimwhite = '#A3A3A3'

# Page Functions
class App:

    # Create new frame function
    def createnewframe(self):
        self.frame = Frame(root)
        self.frame.place(width = 840, height = 480, relx = 0.5, rely = 0.5, anchor = CENTER)

    # Correct/Incorrect miniframe
    def createminiframe(self, miniframetitletext, bgcolor, correctanswertext, currentscoretext):

        # Dim background
        self.title.config(fg = dimwhite, bg = dimblue)
        self.frame.config(bg = dimwhite)

        # Create and place miniframe
        self.miniframe = Frame(root, highlightbackground = bgcolor, highlightthickness = 10)
        self.miniframe.place(width = 360, height = 265, relx = 0.5, rely = 0.5, anchor = CENTER)

        miniframetitle = Label(self.miniframe, text = miniframetitletext, font = ('Comic Sans MS', 40), fg = white, bg = bgcolor)
        miniframetitle.place(width = 360, height = 60, relx = 0.5, rely = 0, anchor = N)

        correctanswer = Label(self.miniframe, text = correctanswertext, font = ('Comic Sans MS', 20), fg = gray)
        correctanswer.place(relx = 0.5, rely = 0.35, anchor = CENTER)

        currentscore = Label(self.miniframe, text = currentscoretext, font = ('Comic Sans MS', 20), fg = gray)
        currentscore.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        nextbutton = Button(self.miniframe, text = "Next", command = self.nextquestion, font = ('Comic Sans MS', 30), fg = white, bg = blue, borderwidth = 12)
        nextbutton.place(width = 180, height = 80, relx = 0.5, rely = 0.8, anchor = CENTER)

    # Close Frame Function
    def closeframe(self):
        self.frame.destroy()

    # Title Label function
    def createtitlelabel(self, titletext):
        self.title = Label(self.frame, text = titletext, font = ('Comic Sans MS', 50), fg = white, bg = blue)
        self.title.place(width = 840, relx = 0.5, rely = 0, anchor = N)

    # Contructor + Name Page
    def __init__(self):
        self.createnewframe()

        # Creating and placing Labels
        self.createtitlelabel("Math Game")
        
        namelabel = Label(self.frame, text = "Name:", font = ('Comic Sans MS', 30), fg = gray)
        namelabel.place(relx = 0.25, rely = 0.5, anchor = CENTER)

        self.nameentry = Entry(self.frame, font = ('Comic Sans MS', 30))
        self.nameentry.place(width = 260, height = 80, relx = 0.5, rely = 0.5, anchor = CENTER)

        nextbutton = Button(self.frame, text = "Next", command = self.verify, font = ('Comic Sans MS', 30), fg = white, bg = blue, borderwidth = 12)
        nextbutton.place(width = 180, height = 80, relx = 0.85, rely = 0.85, anchor = CENTER)

    # Record name as variable and switch frame
    def verify(self):
        self.name = self.nameentry.get()
        
        # If response field is EMPTY
        if self.name == "":

            # Create and place error text under entry box
            errorlabel = Label(self.frame, text = "Enter your name into the box above.", font = ('Comic Sans MS', 20), fg = red)
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
        self.difficultylabels1 = ["+ / - : Up to 100", "+ / - : Up to 100", "+ / - : Up to 1000"]
        self.difficultylabels2 = ["", "x / ÷ : Up to 12" ,"x / ÷ : Up to 100"]

        # Creating and placing Labels
        self.createtitlelabel("Select Difficulty")

        clicktochange = Label(self.frame, text = "Click to Change", font = ('Comic Sans MS', 20), fg = gray)
        clicktochange.place(relx = 0.5, rely = 0.325, anchor = CENTER)

        self.difficultybutton = Button(self.frame, text = "Easy", command = self.changedifficulty, font = ('Comic Sans MS', 30), fg = white, bg = blue, borderwidth = 12)
        self.difficultybutton.place(width = 260, height = 80, relx = 0.5, rely = 0.45, anchor = CENTER)

        self.difficultylabel1 = Label(self.frame, text = "+ / - : Up to 100", font = ('Comic Sans MS', 24), fg = gray)
        self.difficultylabel1.place(relx = 0.5, rely = 0.6, anchor = CENTER)
        self.difficultylabel2 = Label(self.frame, text = "", font = ('Comic Sans MS', 24), fg = gray)
        self.difficultylabel2.place(relx = 0.5, rely = 0.7, anchor = CENTER)

        startbutton = Button(self.frame, text = "Start", command = self.play, font = ('Comic Sans MS', 30), fg = white, bg = green, borderwidth = 12)
        startbutton.place(width = 170, height = 80, relx = 0.85, rely = 0.85, anchor = CENTER)

        backbutton = Button(self.frame, text = "Back", command = self.back, font = ('Comic Sans MS', 30), fg = white, bg = blue, borderwidth = 12)
        backbutton.place(width = 170, height = 80, relx = 0.15, rely = 0.85, anchor = CENTER)

    def back(self):
        self.closeframe()
        self.__init__()
        
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

        # Change difficulty label text
        difficultylabel1 = self.difficultylabels1[self.difficultyindex]
        self.difficultylabel1.config(text = difficultylabel1)

        difficultylabel2 = self.difficultylabels2[self.difficultyindex]
        self.difficultylabel2.config(text = difficultylabel2)
    
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

        # Generate equation and sign
        # Sign index, 0 = Addition, 1 = Subtraction, 2 = Multiplication, 4 = Division
        signindex = random.randint(0, self.signmax)

        # If Addition/Subtraction
        if signindex <= 1:
            numberone = random.randint(0, self.addsubmax)
            numbertwo = random.randint(0, self.addsubmax)
            if signindex == 1:
                sign = "+"
                self.answer = float(numberone + numbertwo)
            else:
                sign = "-"
                self.answer = float(numberone - numbertwo)
        
        # If Multiplication/Division
        else:
            numberone = random.randint(0, self.muldivmax)
            numbertwo = random.randint(0, self.muldivmax)
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
        self.questionindextext = F"Question {self.questionindex} of 10"
        
        # Gameplay Displayed Page Setup
        self.questionindexlabel = self.createtitlelabel(self.questionindextext)
        self.equationlabel = Label(self.frame, text = self.equation, font = ("Arial", 40))
        self.equationlabel.place(relx = 0.5, rely = 0.4, anchor = CENTER)

        self.responseentry = Entry(self.frame, font = ('Comic Sans MS', 30))
        self.responseentry.place(width = 260, height = 80, relx = 0.5, rely = 0.55, anchor = CENTER)

        self.submitbutton = Button(self.frame, text = "Submit", command = self.submit, font = ('Comic Sans MS', 30), fg = white, bg = blue, borderwidth = 12)
        self.submitbutton.place(width = 180, height = 80, relx = 0.5, rely = 0.85, anchor = CENTER)

        self.errorlabel = Label(self.frame, text = "blank", font = ('Comic Sans MS', 20), fg = red)
        self.errorlabel.place(relx = 0.5, rely = 0.7, anchor = CENTER)

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

            # If response field is EMPTY
            if self.response == "":
                self.errorlabel.config(text = "Enter a number into the box above.")
        
            # If invalid response entered
            else:
                self.errorlabel.config(text = F"{self.response} is not a valid number.")

    # If response IS a valid integer
    def markresponse(self):
        
        # Create and place label based on if answer correct or incorrect
        self.submitbutton.config(state = DISABLED, bg = gray)

        if self.response == self.answer:
            self.correctresponses += 1
            self.createminiframe("Correct", green, "", F"{self.correctresponses} for {self.questionindex}")
            
        else:
            self.createminiframe("Incorrect", red, F"{self.equation} = {self.answer}", F"{self.correctresponses} for {self.questionindex}")     
        
    def nextquestion(self):
        self.closeframe()

        # If below question limit
        if self.questionindex < 0:
            self.generatequestion()

        # If question limit reached
        else:
            self.closeframe()
            self.gameover()

            # Create newplayer object in Player class
            newplayer = Player(self.name, self.correctresponses, self.questionindex)

            # Instance of player
            Player.displayprofile(newplayer)
            Player.saveprofile(newplayer)

    def gameover(self):
        self.createnewframe()

        self.createtitlelabel("Game Over")
        scoretextlabel = Label(self.frame, text = "You got             correct", font = ('Comic Sans MS', 40), fg = gray)
        scoretextlabel.place(relx = 0.495, rely = 0.5, anchor = CENTER)
        scorelabel = Label(self.frame, text = F"{self.correctresponses} / 10 ", font = ('Comic Sans MS', 40), fg = blue)
        scorelabel.place(x = 520, y = 240, anchor = E)

        replaybutton = Button(self.frame, text = "Replay", command = self.difficulty, font = ('Comic Sans MS', 30), fg = white, bg = blue, borderwidth = 12)
        replaybutton.place(width = 180, height = 80, relx = 0.15, rely = 0.85, anchor = CENTER)

        nextbutton = Button(self.frame, text = "Continue", command = self.scoreboard, font = ('Comic Sans MS', 30), fg = white, bg = blue, borderwidth = 12)
        nextbutton.place(width = 180, height = 80, relx = 0.85, rely = 0.85, anchor = CENTER)

    def scoreboard(self):
        print("Scoreboard")

# Initialize class and Tkinter root window
App()
root.resizable(False, False)
root.mainloop()
import random
from player import *
from tkinter import *

root = Tk()
root.title("Math Game")
root.geometry("840x480")

# Color Palette
defaultgray = '#F0F0F0'
white = '#FFFFFF'
red = '#FF0000'
gray = '#414141'
green = '#1DD600'
blue = '#4285F4'
paleblue = '#C9DAF8'
#dimred = '#AB2C2C'
#dimgreen = '#2CAB2C'
dimblue = '#48629C'
dimwhite = '#A3A3A3'

fontA = 'Comic Sans MS'
fontB = 'Arial'

class Game:

    # Switch Page Function
    def switchPage(self, targetpage):
        self.frame.destroy()
        self.frame = Frame(root)
        self.frame.place(width = 840, height = 480, relx = 0.5, rely = 0.5, anchor = CENTER)
        targetpage()

    # Verify Name And Age Function
    def verify(self):
        validname = False
        validage = False

        # VERIFY NAME 
        self.name = self.nameentry.get()
        self.name_nospace = self.name.replace(" ", "")
        
        # Set error label text to blank
        self.nameerrorlabel.config(text = "")

        # If response field is EMPTY
        if self.name_nospace == "":
            # Create and place error text under entry box
            self.nameerrorlabel.config(text = "Enter your name into the box above.")
            self.nameentry.delete(0, END)

        # If name entered
        else:
            validname = True

        # VERIFY AGE MODULE
        # Set error text to blank
        self.ageerrorlabel.config(text = "")
        self.age = self.ageentry.get()

        try:
            # Conversions
            self.age_nospace = self.age.replace(" ", "")
        
            if self.age_nospace == "":
                # Configure error text under entry box
                self.ageerrorlabel.config(text = "Enter your age into the box above.")
                self.ageentry.delete(0, END)

            else:
                self.age_intnospace = int(self.age_nospace)
                if self.age_intnospace in range(13, 16):
                    validage = True
                else:
                    self.ageerrorlabel.config(text = "Enter a number between 13 and 15")
                    self.ageentry.delete(0, END)
        except:
            # Configure error text under entry box
            ageerrorlabel = Label(self.frame, text = "Enter a valid number.", font = (fontA, 20), fg = red)
            ageerrorlabel.place(relx = 0.9, rely = 0.1, anchor = CENTER)
            self.ageentry.delete(0, END)

        print(F"Name {validname}. Age {validage}")

        if validname and validage:
            self.switchPage(self.difficultyPage)

    # Title Label Function
    def createTitleLabel(self, titletext):
        self.title = Label(self.frame, text = titletext, font = (fontA, 50), fg = white, bg = blue)
        self.title.place(width = 840, relx = 0.5, rely = 0, anchor = N)

    # Change Difficulty Function
    def changeDifficulty(self):
        
        if self.difficultyindex <= 1:
            self.difficultyindex += 1
        else:
            self.difficultyindex = 0
        print(F"changeDifficulty: Difficulty Index Changed to {self.difficultyindex}")

        # Change difficulty button text 
        difficulty = self.difficulties[self.difficultyindex]
        self.difficultybutton.config(text = difficulty)

        # Change difficulty label text
        difficultylabel1 = self.difficultylabels1[self.difficultyindex]
        self.difficultylabel1.config(text = difficultylabel1)

        difficultylabel2 = self.difficultylabels2[self.difficultyindex]
        self.difficultylabel2.config(text = difficultylabel2)

    # Initialize Game Function (Setting variables)
    def initializeGame(self):

        # Set variables
        self.questionindex = 1
        print(F"Question Index set to {self.questionindex}")
        self.correct = 0

        # Create progress bar frame
        self.barframe = Frame(root)
        self.barframe.place(width = 840, height = 20, x = 420, y = 120, anchor = CENTER)
        
        # Define bar widgets (Placement in initializeGame ensures new set of bars are not created each question)
        self.bar1 = Label(self.barframe, text = "", fg = white, bg = gray, font = (fontA, 15))
        self.bar2 = Label(self.barframe, text = "", fg = white, bg = gray, font = (fontA, 15))
        self.bar3 = Label(self.barframe, text = "", fg = white, bg = gray, font = (fontA, 15))
        self.bar4 = Label(self.barframe, text = "", fg = white, bg = gray, font = (fontA, 15))
        self.bar5 = Label(self.barframe, text = "", fg = white, bg = gray, font = (fontA, 15))
        self.bar6 = Label(self.barframe, text = "", fg = white, bg = gray, font = (fontA, 15))
        self.bar7 = Label(self.barframe, text = "", fg = white, bg = gray, font = (fontA, 15))
        self.bar8 = Label(self.barframe, text = "", fg = white, bg = gray, font = (fontA, 15))
        self.bar9 = Label(self.barframe, text = "", fg = white, bg = gray, font = (fontA, 15))
        self.bar10 = Label(self.barframe, text = "", fg = white, bg = gray, font = (fontA, 15))

        # Place progress bars
        self.bar1.place(height = 20, width = 70, x =  + 40, y = 0, anchor = N)
        self.bar2.place(height = 20, width = 70, x = 84 + 40, y = 0, anchor = N)
        self.bar3.place(height = 20, width = 70, x = 84 * 2 + 40, y = 0, anchor = N)
        self.bar4.place(height = 20, width = 70, x = 84 * 3 + 40, y = 0, anchor = N)
        self.bar5.place(height = 20, width = 70, x = 84 * 4 + 40, y = 0, anchor = N)
        self.bar6.place(height = 20, width = 70, x = 84 * 5 + 40, y = 0, anchor = N)
        self.bar7.place(height = 20, width = 70, x = 84 * 6 + 40, y = 0, anchor = N)
        self.bar8.place(height = 20, width = 70, x = 84 * 7 + 40, y = 0, anchor = N)
        self.bar9.place(height = 20, width = 70, x = 84 * 8 + 40, y = 0, anchor = N)
        self.bar10.place(height = 20, width = 70, x = 84 * 9 + 40, y = 0, anchor = N)

        # Create list for bars
        self.bars = [self.bar1, self.bar2, self.bar3, self.bar4, self.bar5, self.bar6, self.bar7, self.bar8, self.bar9, self.bar10]

        # Generate first question
        self.generateQuestion()

    # Generate Question Function
    def generateQuestion(self):

        # Set ranges based on difficulty
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

        # Generate equation and sign
        # Sign index, 0 = Addition, 1 = Subtraction, 2 = Multiplication, 4 = Division
        signindex = random.randint(0, self.signmax)

        # If Addition/Subtraction
        if signindex <= 1:
            self.numberone = random.randint(0, self.addsubmax)
            self.numbertwo = random.randint(0, self.addsubmax)
            if signindex == 1:
                self.sign = "+"
                self.answer = float(self.numberone + self.numbertwo)
            else:
                self.sign = "-"
                self.answer = float(self.numberone - self.numbertwo)
        
        # If Multiplication/Division
        else:
            self.numberone = random.randint(1, self.muldivmax)
            self.numbertwo = random.randint(0, self.muldivmax)
            if signindex == 3:
                self.sign = "×"
                self.answer = float(self.numberone * self.numbertwo)
            else:
                self.sign = "÷"

                # Logic to make sure answer is a whole number
                self.numberone = self.numberone * self.numbertwo
                self.answer = float(self.numberone / self.numbertwo)

        # Initiate question page
        print(F"generateQuestion: {self.answer}")
        self.switchPage(self.questionPage)

    # Submit Response Function
    def submit(self):

        # Record response as variable
        self.response = self.responseentry.get()
        self.response = self.response.replace(" ", "")

        # Try if response is valid number
        try:
            self.response = float(self.responseentry.get())
            self.markResponse()

        # If response is NOT a valid number
        except ValueError:

            # If response field is EMPTY
            if self.response == "":
                self.errorlabel.config(text = "Enter a number into the box above.")
                self.responseentry.delete(0, END)
        
            # If invalid response entered
            else:
                self.errorlabel.config(text = F"{self.response} is not a valid number.")
                self.responseentry.delete(0, END)

    # Mark Response Function
    def markResponse(self):
        
        # Create and place label based on if answer correct or incorrect
        self.submitbutton.config(state = DISABLED, bg = gray)

        # Correct answer
        if self.response == self.answer:
            self.correct += 1
            self.resultPage("Correct", green, "", F"{self.correct} for {self.questionindex}", 30, 0.45)
            self.barcolor = green
            self.bartext = "✔"

        # Incorrect answer
        else:
            self.resultPage("Incorrect", red, "{} = {:,g}".format(F"{self.numberone} {self.sign} {self.numbertwo}", self.answer), F"{self.correct} for {self.questionindex}", 20, 0.5)
            self.barcolor = red
            self.bartext = "✖"

    # Next Question Function
    def nextQuestion(self):

        # If below question limit
        if self.questionindex < 10:

            # Undo dim barframe (Frame is not destroyed like questionPage and resultPage frames)
            self.barframe.config(bg = defaultgray)

            # Change bar color
            self.changebar = self.bars[self.questionindex - 1]
            self.changebar.config(bg = self.barcolor, text = self.bartext)

            # Add to question index
            self.questionindex += 1
            print(F"nextQuestion: Question Index changed to {self.questionindex}")

            # Generate another question
            self.switchPage(self.generateQuestion)

        # If question limit reached
        else:

            # Initialize Game Over Page Function
            self.switchPage(self.gameOverPage)

            # Destroy barframe
            self.barframe.destroy()

    # Store Profile Function  
    def storeProfiles(self):

        # Open savedprofiles.txt file
        self.savedprofiles = open('savedprofiles.txt', 'a')

        # Format correct before saving
        self.correct = "{:02d}".format(self.correct)

        # Create saveplayer object in Player class
        saveplayer = Player(self.name, self.correct, self.difficulties[self.difficultyindex], self.age_intnospace)

        # Log instance of player
        Player.saveProfile(saveplayer)
        self.savedprofiles.close()

        # Compile list of profile objects 
        self.savedprofiles = open('savedprofiles.txt').readlines()
        self.profiles = []
        for line in self.savedprofiles:
            row = line.split(',')
            name, correct, difficulty, age = [i.strip() for i in row]
            profile = Player(name, correct, difficulty, age)
            self.profiles = self.profiles + [profile]

        # Sort by highest to lowest correct answers
        self.profiles.sort(key=lambda x: x.savecorrect, reverse=True)

        # Truncate list to top 5 scorers
        self.profiles = self.profiles[:5]

    # CONSTRUCTOR
    def __init__(self):
        self.name = ""
        self.namePage()

    # Name Page
    def namePage(self):

        # Create initial frame
        self.frame = Frame(root)
        self.frame.place(width = 840, height = 480, relx = 0.5, rely = 0.5, anchor = CENTER)

        # Create Title Label
        self.createTitleLabel("Math Game")
        
        # Defining label, entry and button
        namelabel = Label(self.frame, text = "Name:", font = (fontA, 30), fg = gray)
        self.nameentry = Entry(self.frame, font = (fontB, 30))
        self.nameerrorlabel = Label(self.frame, text = "", font = (fontA, 20), fg = red)
        agelabel = Label(self.frame, text = "Age:", font = (fontA, 25), fg = white, bg = blue)
        self.ageentry = Entry(self.frame, font = (fontB, 25))
        self.ageerrorlabel = Label(self.frame, text = "", font = (fontA, 15), fg = red)
        nextbutton = Button(self.frame, text = "Next", command = self.verify, font = (fontA, 25), fg = white, bg = blue, borderwidth = 12)

        # Enter previously entered name on repeat visits
        self.nameentry.insert(0, self.name)

        # Place widgets
        namelabel.place(relx = 0.25, rely = 0.5, anchor = CENTER)
        self.nameentry.place(width = 260, height = 80, relx = 0.5, rely = 0.5, anchor = CENTER)
        self.nameerrorlabel.place(relx = 0.5, rely = 0.65, anchor = CENTER)
        agelabel.place(relx = 0.85, rely = 0.1, anchor = CENTER)
        self.ageentry.place(width = 60, height = 60, relx = 0.95, rely = 0.1, anchor = CENTER)
        self.ageerrorlabel.place(relx = 0.8, rely = 0.25, anchor = CENTER)
        nextbutton.place(width = 180, height = 80, relx = 0.85, rely = 0.85, anchor = CENTER)

    # Difficulty Page
    def difficultyPage(self):

        # Create and place title widget
        self.createTitleLabel("Select Difficulty")

        # Setting starting variables for Change Difficulty Function Loop
        self.difficultyindex = 0
        print(F"difficultyPage: Difficulty Index Set to 0")
        self.difficulties = ["Easy", "Medium", "Hard"]
        self.difficultylabels1 = ["+ / - : Up to 100", "+ / - : Up to 100", "+ / - : Up to 1000"]
        self.difficultylabels2 = ["", "x / ÷ : Up to 12" ,"x / ÷ : Up to 100"]

        # Define widgets
        clicktochange = Label(self.frame, text = "Click to Change", font = (fontA, 20), fg = gray)
        self.difficultybutton = Button(self.frame, text = "Easy", command = self.changeDifficulty, font = (fontA, 30), fg = white, bg = blue, borderwidth = 12)
        self.difficultylabel1 = Label(self.frame, text = "+ / - : Up to 100", font = (fontA, 24), fg = gray)
        self.difficultylabel2 = Label(self.frame, text = "", font = (fontA, 24), fg = gray)
        startbutton = Button(self.frame, text = "Start", command = self.initializeGame, font = (fontA, 25), fg = white, bg = green, borderwidth = 12)
        backbutton = Button(self.frame, text = "Back", command = lambda: self.switchPage(self.namePage), font = (fontA, 25), fg = white, bg = blue, borderwidth = 12)
        
        # Place widgets
        clicktochange.place(relx = 0.5, rely = 0.325, anchor = CENTER)
        self.difficultybutton.place(width = 260, height = 80, relx = 0.5, rely = 0.45, anchor = CENTER)
        self.difficultylabel1.place(relx = 0.5, rely = 0.6, anchor = CENTER)
        self.difficultylabel2.place(relx = 0.5, rely = 0.7, anchor = CENTER)
        startbutton.place(width = 170, height = 80, relx = 0.85, rely = 0.85, anchor = CENTER)
        backbutton.place(width = 170, height = 80, relx = 0.15, rely = 0.85, anchor = CENTER)

    # Question Page
    def questionPage(self):

        # Create and place title widget (Define under variable as it must be configurable)
        self.questionindexlabel = self.createTitleLabel(F"Question {self.questionindex} of 10")

        # Define widgets
        self.equationlabel = Label(self.frame, text = F"{self.numberone} {self.sign} {self.numbertwo}", font = (fontB, 40))
        self.responseentry = Entry(self.frame, font = (fontB, 30))
        self.submitbutton = Button(self.frame, text = "Submit", command = self.submit, font = (fontA, 30), fg = white, bg = blue, borderwidth = 12)
        
        # Place widgets
        self.errorlabel = Label(self.frame, text = "", font = (fontA, 20), fg = red)
        self.equationlabel.place(relx = 0.5, rely = 0.4, anchor = CENTER)
        self.responseentry.place(width = 260, height = 80, relx = 0.5, rely = 0.55, anchor = CENTER)
        self.submitbutton.place(width = 180, height = 80, relx = 0.5, rely = 0.85, anchor = CENTER)
        self.errorlabel.place(relx = 0.5, rely = 0.7, anchor = CENTER)

        # Raise barframe over questionPage frame
        self.barframe.tkraise()

    # Result Page
    def resultPage(self, miniframetitletext, bgcolor, correctanswertext, currentscoretext, currentscoresize, currentscoreheight):

        # Dim questionPage frame and barframe colors
        self.title.config(fg = dimwhite, bg = dimblue)
        self.frame.config(bg = dimwhite)
        self.barframe.config(bg = dimwhite)

        # Define widgets
        self.miniframe = Frame(root, highlightbackground = bgcolor, highlightthickness = 10)
        miniframetitle = Label(self.miniframe, text = miniframetitletext, font = (fontA, 40), fg = white, bg = bgcolor)
        correctanswer = Label(self.miniframe, text = correctanswertext, font = (fontA, 20), fg = gray)
        currentscore = Label(self.miniframe, text = currentscoretext, font = (fontA, currentscoresize), fg = gray)
        nextbutton = Button(self.miniframe, text = "Next", command = self.nextQuestion, font = (fontA, 25), fg = white, bg = blue, borderwidth = 12)
        
        # Place widgets
        self.miniframe.place(width = 360, height = 265, relx = 0.5, rely = 0.5, anchor = CENTER)
        miniframetitle.place(width = 360, height = 60, relx = 0.5, rely = 0, anchor = N)
        correctanswer.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        currentscore.place(relx = 0.5, rely = currentscoreheight, anchor = CENTER)
        nextbutton.place(width = 180, height = 80, relx = 0.5, rely = 0.8, anchor = CENTER)

    # Game Over Page
    def gameOverPage(self):

        # Create and place title label
        self.createTitleLabel("Game Over")

        # Define widgets
        scoretextlabel = Label(self.frame, text = "You got             correct", font = (fontA, 40), fg = gray)
        scorelabel = Label(self.frame, text = F"{self.correct} / 10 ", font = (fontA, 40), fg = blue)
        replaybutton = Button(self.frame, text = "Replay", command = lambda: self.switchPage(self.difficultyPage), font = (fontA, 25), fg = white, bg = blue, borderwidth = 12)
        continuebutton = Button(self.frame, text = "Continue", command = lambda: self.switchPage(self.scoreboardPage), font = (fontA, 25), fg = white, bg = blue, borderwidth = 12)

        # Place widgets
        scoretextlabel.place(relx = 0.495, rely = 0.5, anchor = CENTER)
        scorelabel.place(x = 520, y = 240, anchor = E)
        replaybutton.place(width = 180, height = 80, relx = 0.15, rely = 0.85, anchor = CENTER)
        continuebutton.place(width = 180, height = 80, relx = 0.85, rely = 0.85, anchor = CENTER)

        # Initialize profile storing
        self.storeProfiles()
    
    # New Player Function
    def newPlayer(self):
        self.name = ""
        self.switchPage(self.namePage)

    # Scoreboard Page
    def scoreboardPage(self):

        # Create title label
        self.createTitleLabel("Scoreboard")

        # Defining table
        scoretable = Frame(self.frame, bg = red)

        # Define rows
        row0 = Frame(scoretable, width = 840, height = 40, bg = dimblue)
        row1 = Frame(scoretable, width = 840, height = 40, bg = paleblue)
        row2 = Frame(scoretable, width = 840, height = 40, bg = white)
        row3 = Frame(scoretable, width = 840, height = 40, bg = paleblue)
        row4 = Frame(scoretable, width = 840, height = 40, bg = white)
        row5 = Frame(scoretable, width = 840, height = 40, bg = paleblue)

        # Define top row labels
        scoretablename = Label(scoretable, text = "Name", font = (fontA, 16), fg = white, bg = dimblue)
        scoretablepct = Label(scoretable, text = "Correct", font = (fontA, 16), fg = white, bg = dimblue)
        scoretabledifficulty = Label(scoretable, text = "Difficulty", font = (fontA, 16), fg = white, bg = dimblue)
        gridy = 40

        for index, value in enumerate(self.profiles):
            
            # To make rows alternative color
            if gridy == 80 or gridy == 160:
                alternating = white
            else:
                alternating = paleblue

            # Define labels
            col0 = Label(scoretable, text = self.profiles[index].savename, width = 0, font = (fontA, 16), bg = alternating)
            col1 = Label(scoretable, text = F"{self.profiles[index].savecorrect}0%".strip("0"), font = (fontA, 16), bg = alternating)
            col2 = Label(scoretable, text = self.profiles[index].savedifficulty, font = (fontA, 16), bg = alternating)

            # Place labels
            col0.place(x = 0, y = gridy, anchor = NW)
            col1.place(x = 280, y = gridy, anchor = NW)
            col2.place(x = 560, y = gridy, anchor = NW)
            
            gridy += 40

        # Defining widgets
        replaybutton = Button(self.frame, text = "Replay", command = lambda: self.switchPage(self.difficultyPage), font = (fontA, 25), fg = white, bg = blue, borderwidth = 12)
        newplayerbutton = Button(self.frame, text = "New Player", command = self.newPlayer, font = (fontA, 25), fg = white, bg = blue, borderwidth = 12)

        # Place scoreboard rows
        row0.place(x = 0, y = 0, anchor = NW)
        row1.place(x = 0, y = 40, anchor = NW)
        row2.place(x = 0, y = 80, anchor = NW)
        row3.place(x = 0, y = 120, anchor = NW)
        row4.place(x = 0, y = 160, anchor = NW)
        row5.place(x = 0, y = 200, anchor = NW)

        # Place scoreboard title words
        scoretable.place(relx = 0.5, rely = 0.45, width = 840, height = 240, anchor = CENTER)
        scoretablename.place(x = 0, y = 0, anchor = NW)
        scoretablepct.place(x = 280, y = 0, anchor = NW)
        scoretabledifficulty.place(x = 560, y = 0, anchor = NW)

        # Place button widgets
        replaybutton.place(width = 180, height = 80, relx = 0.15, rely = 0.85, anchor = CENTER)
        newplayerbutton.place(width = 240, height = 80, relx = 0.80, rely = 0.85, anchor = CENTER)

# Initialize program and Tkinter root window
Game()
root.resizable(False, False)
root.mainloop()
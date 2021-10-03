import random
from player import *
from tkinter import *

root = Tk()
root.title("Math Game")
root.geometry("840x480")

# Light Palette
textcolorA_light = '#FFFFFF'
textcolorB_light = '#414141'
textcolorC_light = '#000000'
dimtextcolorA_light = '#B5B5B5'

framebgcolor_light = '#F0F0F0'
red_light = '#FF0000'
green_light = '#1DD600'
secondarycolor_light = '#4285F4'
dimred_light = '#AB2C2C'
dimgreen_light = '#2CAB2C'
dimsecondarycolor_light = '#2E5EAD'
dimframebgcolor_light = '#AAAAAA'
buttoncolor_disabled_light = '#525252'
barcolor_blank_light = '#CCCCCC'
dimbarcolor_blank_light = '#909090'
scoreboardcolorA_light = '#FFFFFF'
scoreboardcolorB_light = '#C9DAF8'

# Dark Palette
textcolor_dark = '#FFFFFF'
dimtextcolor_dark = '#939393'
framebgcolor_dark = '#202020'
#secondarycolor_dark = '#4C5073'
secondarycolor_dark = '#686085'
dimred_dark = '#930000'
dimgreen_dark = '#107B00'
dimsecondarycolor_dark = '#3B374C'
dimframebgcolor_dark = '#121212'
barcolor_blank_dark = '#555555'
dimbarcolor_blank_dark = '#313131'
scoreboardcolorA_dark = '#101010'
scoreboardcolorB_dark = '#000000'

# Define fonts
fontA = 'Comic Sans MS'
fontB = 'Arial'

# Load icons
sun_icon = PhotoImage(file = "sun_icon.png")
moon_icon = PhotoImage(file = "moon_icon.png")

class Game:

    # Switch Page Function
    def switchPage(self, targetpage):
        self.frame.destroy()
        self.frame = Frame(root, bg = self.framebgcolor)
        self.frame.place(width = 840, height = 480, relx = 0.5, rely = 0.5, anchor = CENTER)
        targetpage()

    # Selected Palette
    def switchPalette(self):

        # Dark Mode to Light Mode
        if self.darkmode:
            self.textcolorA = textcolorA_light
            self.textcolorB = textcolorB_light
            self.textcolorC = textcolorC_light
            self.dimtextcolorA = dimtextcolorA_light
            self.framebgcolor = framebgcolor_light
            self.red = red_light
            self.textcolorA = textcolorA_light
            self.green = green_light
            self.secondarycolor = secondarycolor_light
            self.dimred = dimred_light
            self.dimgreen = dimgreen_light
            self.dimbarcolor_blank = dimbarcolor_blank_light
            self.dimsecondarycolor = dimsecondarycolor_light
            self.dimframebgcolor = dimframebgcolor_light
            self.darkmode = False
            self.switchPage(self.namePage)
            self.switchpaletteicon = sun_icon
            self.switchpalettebutton.config(image = self.switchpaletteicon)
        
        # Light Mode to Dark Mode
        else:
            self.textcolorA = textcolor_dark
            self.textcolorB = textcolor_dark
            self.textcolorC = textcolor_dark
            self.dimtextcolorA = dimtextcolor_dark
            self.framebgcolor = framebgcolor_dark
            self.textcolorA = textcolor_dark
            self.secondarycolor = secondarycolor_dark
            self.barcolor_blank = barcolor_blank_dark
            self.dimred = dimred_dark
            self.dimgreen = dimgreen_dark
            self.dimsecondarycolor = dimsecondarycolor_dark
            self.dimframebgcolor = dimframebgcolor_dark
            self.dimbarcolor_blank = dimbarcolor_blank_dark
            self.scoreboardcolorA = scoreboardcolorA_dark
            self.scoreboardcolorB = scoreboardcolorB_dark
            self.darkmode = True
            self.switchPage(self.namePage)
            self.switchpaletteicon = moon_icon
            self.switchpalettebutton.config(image = self.switchpaletteicon)

    # Verify Name And Age Function
    def verify(self):
        # Get inputs from widgets
        self.name = self.nameentry.get()
        self.age = self.ageentry.get()

        # Initialize name and age value
        currentplayer = Player(self.name, 0, 'N/A', self.age)

        # Configure labels using returned tuple values
        returnvalues = Player.validate(currentplayer)
        self.nameerrorlabel.config(text = returnvalues[1])
        self.ageerrorlabel.config(text = returnvalues[2])

        # Switch page if both inputs valid
        if returnvalues[0]:
            self.switchPage(self.difficultyPage)

    # Title Label Function
    def createTitleLabel(self, titletext):
        self.title = Label(self.frame, text = titletext, font = (fontA, 50), fg = self.textcolorA, bg = self.secondarycolor)
        self.title.place(width = 840, relx = 0.5, rely = 0, anchor = N)

    # Change Difficulty Function
    def changeDifficulty(self):
        
        if self.difficultyindex == 2:
            self.difficultyindex = 0
        else:
            self.difficultyindex += 1

        # Change difficulty button text 
        self.difficultybutton.config(text = self.difficulties[self.difficultyindex])

        # Change difficulty descriptions text
        self.difficultylabel1.config(text = self.difficultylabels1[self.difficultyindex])
        self.difficultylabel2.config(text = self.difficultylabels2[self.difficultyindex])

    # Initialize Game Function (Setting variables)
    def initiateGame(self):

        # Set variables
        self.questionindex = 1
        self.correct = 0

        # Create redbars and greenbars lists
        self.redbars = []
        self.greenbars = []

        # Create progress bar frame
        self.barframe = Frame(root, bg = self.framebgcolor)
        self.barframe.place(width = 840, height = 20, x = 420, y = 120, anchor = CENTER)
        
        # Define bar widgets (Placement in initiateGame ensures new set of bars are not created each question)
        self.bar1 = Label(self.barframe, text = "", fg = self.textcolorB, bg = self.barcolor_blank, font = (fontA, 15))
        self.bar2 = Label(self.barframe, text = "", fg = self.textcolorB, bg = self.barcolor_blank, font = (fontA, 15))
        self.bar3 = Label(self.barframe, text = "", fg = self.textcolorB, bg = self.barcolor_blank, font = (fontA, 15))
        self.bar4 = Label(self.barframe, text = "", fg = self.textcolorB, bg = self.barcolor_blank, font = (fontA, 15))
        self.bar5 = Label(self.barframe, text = "", fg = self.textcolorB, bg = self.barcolor_blank, font = (fontA, 15))
        self.bar6 = Label(self.barframe, text = "", fg = self.textcolorB, bg = self.barcolor_blank, font = (fontA, 15))
        self.bar7 = Label(self.barframe, text = "", fg = self.textcolorB, bg = self.barcolor_blank, font = (fontA, 15))
        self.bar8 = Label(self.barframe, text = "", fg = self.textcolorB, bg = self.barcolor_blank, font = (fontA, 15))
        self.bar9 = Label(self.barframe, text = "", fg = self.textcolorB, bg = self.barcolor_blank, font = (fontA, 15))
        self.bar10 = Label(self.barframe, text = "", fg = self.textcolorB, bg = self.barcolor_blank, font = (fontA, 15))

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

    def generateQuestion(self):
        # Initialize difficulty
        currentplayer = Player(self.name, 0, self.difficulty, self.age)

        # Return tuple 
        returnvalues = Player.generateQuestion(currentplayer)
        self.numberone = (returnvalues[0])
        self.numbertwo = (returnvalues[1])
        self.sign = (returnvalues[2])
        self.answer = (returnvalues[3])

        # Initiate question page
        print(self.answer)
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
        self.submitbutton.config(state = DISABLED, bg = self.buttoncolor_disabled)

        # Correct answer
        if self.response == self.answer:
            self.correct += 1
            self.resultPage("Correct", self.green, "", F"{self.correct} for {self.questionindex}", 30, 0.45)
            self.barcolor = self.green
            self.greenbars.append(self.bars[self.questionindex - 1])
            self.bartext = "✔"

        # Incorrect answer
        else:
            self.resultPage("Incorrect", self.red, "{} = {:,g}".format(F"{self.numberone} {self.sign} {self.numbertwo}", self.answer), F"{self.correct} for {self.questionindex}", 20, 0.5)
            self.barcolor = self.red
            self.redbars.append(self.bars[self.questionindex - 1])
            self.bartext = "✖"

    # Next Question Function
    def nextQuestion(self):

        # If below question limit
        if self.questionindex < 10:

            # Undo dim barframe (Frame is not destroyed like questionPage and resultPage frames)
            self.barframe.config(bg = self.framebgcolor)
            for x in self.bars:
                x.config(bg = self.barcolor_blank)

            for x in self.redbars:
                x.config(bg = self.red, fg = self.textcolorA)

            for x in self.greenbars:
                x.config(bg = self.green, fg = self.textcolorA)

            # Change bar color
            self.bars[self.questionindex - 1].config(bg = self.barcolor, text = self.bartext)

            # Add to question index
            self.questionindex += 1

            # Generate another question
            self.switchPage(self.generateQuestion)

        # If question limit reached
        else:

            # Initialize Game Over Page Function
            for widget in root.winfo_children():
                widget.destroy()
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
        saveplayer = Player(self.name, self.correct, self.difficulties[self.difficultyindex], self.age)

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

        # Set initial color palette
        self.textcolorA = textcolorA_light
        self.textcolorB = textcolorB_light
        self.textcolorC = textcolorC_light
        self.dimtextcolorA = dimtextcolorA_light
        self.framebgcolor = framebgcolor_light
        self.red = red_light
        self.textcolorA = textcolorA_light
        self.green = green_light
        self.secondarycolor = secondarycolor_light
        self.dimred = dimred_light
        self.dimgreen = dimgreen_light
        self.dimsecondarycolor = dimsecondarycolor_light
        self.dimframebgcolor = dimframebgcolor_light
        self.barcolor_blank = barcolor_blank_light
        self.dimbarcolor_blank = dimbarcolor_blank_light
        self.buttoncolor_disabled = buttoncolor_disabled_light
        self.scoreboardcolorA = scoreboardcolorA_light
        self.scoreboardcolorB = scoreboardcolorB_light
        self.switchpaletteicon = sun_icon

        self.darkmode = False

        # Initiate Name page
        self.namePage()

    # Name Page
    def namePage(self):

        # Create initial frame
        self.frame = Frame(root, bg = self.framebgcolor)
        self.frame.place(width = 840, height = 480, relx = 0.5, rely = 0.5, anchor = CENTER)

        # Create Title Label
        self.createTitleLabel("Math Game")
        
        # Defining widgets
        self.switchpalettebutton = Button(self.frame, image = self.switchpaletteicon, command = self.switchPalette, font = (fontA, 25), fg = self.textcolorA, bg = self.secondarycolor, borderwidth = 8)
        namelabel = Label(self.frame, text = "Name:", font = (fontA, 30), fg = self.textcolorB, bg = self.framebgcolor)
        self.nameentry = Entry(self.frame, font = (fontB, 30))
        self.nameerrorlabel = Label(self.frame, text = "", font = (fontA, 20), fg = self.red, bg = self.framebgcolor)
        agelabel = Label(self.frame, text = "Age:", font = (fontA, 25), fg = self.textcolorA, bg = self.secondarycolor)
        self.ageentry = Entry(self.frame, font = (fontB, 25))
        self.ageerrorlabel = Label(self.frame, text = "", font = (fontA, 15), fg = self.red, bg = self.framebgcolor)
        nextbutton = Button(self.frame, text = "Next", command = self.verify, font = (fontA, 25), fg = self.textcolorA, bg = self.secondarycolor, borderwidth = 12)

        # Enter previously entered name on repeat visits
        self.nameentry.insert(0, self.name)

        # Place widgets
        self.switchpalettebutton.place(width = 72, height = 72, relx = 0.1, rely = 0.85, anchor = CENTER)
        namelabel.place(relx = 0.25, rely = 0.5, anchor = CENTER)
        self.nameentry.place(width = 260, height = 80, relx = 0.5, rely = 0.5, anchor = CENTER)
        self.nameerrorlabel.place(relx = 0.5, rely = 0.65, anchor = CENTER)
        agelabel.place(relx = 0.85, rely = 0.1, anchor = CENTER)
        self.ageentry.place(width = 60, height = 60, relx = 0.95, rely = 0.1, anchor = CENTER)
        self.ageerrorlabel.place(relx = 0.98, rely = 0.25, anchor = E)
        nextbutton.place(width = 180, height = 80, relx = 0.85, rely = 0.85, anchor = CENTER)

    # Difficulty Page
    def difficultyPage(self):

        # Create and place title widget
        self.createTitleLabel("Select Difficulty")

        # Setting starting variables for Change Difficulty Function Loop
        self.difficulties = ["Easy", "Medium", "Hard"]
        self.difficultyindex = 0
        self.difficulty = self.difficulties[self.difficultyindex]
        
        self.difficultylabels1 = ["+ / - : Up to 100", "+ / - : Up to 100", "+ / - : Up to 1000"]
        self.difficultylabels2 = ["", "x / ÷ : Up to 12" ,"x / ÷ : Up to 100"]

        # Define widgets
        clicktochange = Label(self.frame, text = "Click to Change", font = (fontA, 20), fg = self.textcolorB, bg = self.framebgcolor)
        self.difficultybutton = Button(self.frame, text = self.difficulty, command = self.changeDifficulty, font = (fontA, 30), fg = self.textcolorA, bg = self.secondarycolor, borderwidth = 12)
        self.difficultylabel1 = Label(self.frame, text = self.difficultylabels1[self.difficultyindex], font = (fontA, 24), fg = self.textcolorB, bg = self.framebgcolor)
        self.difficultylabel2 = Label(self.frame, text = self.difficultylabels2[self.difficultyindex], font = (fontA, 24), fg = self.textcolorB, bg = self.framebgcolor)
        startbutton = Button(self.frame, text = "Start", command = self.initiateGame, font = (fontA, 25), fg = self.textcolorA, bg = self.green, borderwidth = 12)
        backbutton = Button(self.frame, text = "Back", command = lambda: self.switchPage(self.namePage), font = (fontA, 25), fg = self.textcolorA, bg = self.secondarycolor, borderwidth = 12)
        
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
        self.equationlabel = Label(self.frame, text = F"{self.numberone} {self.sign} {self.numbertwo}", font = (fontB, 40), bg = self.framebgcolor, fg = self.textcolorC)
        self.responseentry = Entry(self.frame, font = (fontB, 30))
        self.submitbutton = Button(self.frame, text = "Submit", command = self.submit, font = (fontA, 30), fg = self.textcolorA, bg = self.secondarycolor, borderwidth = 12)
        self.errorlabel = Label(self.frame, text = "", font = (fontA, 20), fg = self.red, bg = self.framebgcolor)

        # Place widgets
        self.equationlabel.place(relx = 0.5, rely = 0.4, anchor = CENTER)
        self.responseentry.place(width = 260, height = 80, relx = 0.5, rely = 0.55, anchor = CENTER)
        self.submitbutton.place(width = 180, height = 80, relx = 0.5, rely = 0.85, anchor = CENTER)
        self.errorlabel.place(relx = 0.5, rely = 0.7, anchor = CENTER)

        # Raise barframe over questionPage frame
        self.barframe.tkraise()

    # Result Page
    def resultPage(self, miniframetitletext, bgcolor, correctanswertext, currentscoretext, currentscoresize, currentscoreheight):

        # Dim questionPage frame and barframe colors
        self.title.config(fg = self.dimtextcolorA, bg = self.dimsecondarycolor)
        self.frame.config(bg = self.dimframebgcolor)
        self.barframe.config(bg = self.dimframebgcolor)
        self.errorlabel.config(bg = self.dimframebgcolor, fg = self.dimred)

        for x in self.bars:
            x.config(bg = self.dimbarcolor_blank)

        for x in self.redbars:
            x.config(bg = self.dimred, fg = self.dimtextcolorA)

        for x in self.greenbars:
            x.config(bg = self.dimgreen, fg = self.dimtextcolorA)

        # Define widgets
        self.miniframe = Frame(root, bg = self.framebgcolor, highlightbackground = bgcolor, highlightthickness = 8)
        miniframetitle = Label(self.miniframe, text = miniframetitletext, font = (fontA, 35), fg = self.textcolorA, bg = bgcolor)
        correctanswer = Label(self.miniframe, text = correctanswertext, font = (fontA, 20), fg = self.textcolorB, bg = self.framebgcolor)
        currentscore = Label(self.miniframe, text = currentscoretext, font = (fontA, currentscoresize), fg = self.textcolorB, bg = self.framebgcolor)
        nextbutton = Button(self.miniframe, text = "Next", command = self.nextQuestion, font = (fontA, 25), fg = self.textcolorA, bg = self.secondarycolor, borderwidth = 12)
        
        # Place widgets
        self.miniframe.place(width = 360, height = 265, relx = 0.5, rely = 0.5, anchor = CENTER)
        miniframetitle.place(width = 360, height = 60, relx = 0.5, y = 0, anchor = N)
        correctanswer.place(relx = 0.5, rely = 0.35, anchor = CENTER)
        currentscore.place(relx = 0.5, rely = currentscoreheight, anchor = CENTER)
        nextbutton.place(width = 180, height = 80, relx = 0.5, rely = 0.8, anchor = CENTER)

    # Game Over Page
    def gameOverPage(self):

        # Create and place title label
        self.createTitleLabel("Game Over")

        # Define widgets
        scoretextlabel = Label(self.frame, text = "You got             correct", font = (fontA, 40), fg = self.textcolorC, bg = self.framebgcolor)
        scorelabel = Label(self.frame, text = F"{self.correct} / 10 ", font = (fontA, 40), fg = self.secondarycolor, bg = self.framebgcolor)
        replaybutton = Button(self.frame, text = "Replay", command = lambda: self.switchPage(self.difficultyPage), font = (fontA, 25), fg = self.textcolorA, bg = self.secondarycolor, borderwidth = 12)
        continuebutton = Button(self.frame, text = "Continue", command = lambda: self.switchPage(self.scoreboardPage), font = (fontA, 25), fg = self.textcolorA, bg = self.secondarycolor, borderwidth = 12)

        # Place widgets
        scoretextlabel.place(relx = 0.495, rely = 0.5, anchor = CENTER)
        scorelabel.place(x = 520, y = 240, anchor = E)
        replaybutton.place(width = 180, height = 80, relx = 0.15, rely = 0.85, anchor = CENTER)
        continuebutton.place(width = 180, height = 80, relx = 0.85, rely = 0.85, anchor = CENTER)

        # Initiate profile storing
        self.storeProfiles()

    # Scoreboard Page
    def scoreboardPage(self):

        # Create title label
        self.createTitleLabel("Scoreboard")

        # Defining table
        scoretable = Frame(self.frame, bg = self.red)

        # Define rows
        row0 = Frame(scoretable, width = 840, height = 40, bg = self.dimsecondarycolor)
        row1 = Frame(scoretable, width = 840, height = 40, bg = self.scoreboardcolorB)
        row2 = Frame(scoretable, width = 840, height = 40, bg = self.scoreboardcolorA)
        row3 = Frame(scoretable, width = 840, height = 40, bg = self.scoreboardcolorB)
        row4 = Frame(scoretable, width = 840, height = 40, bg = self.scoreboardcolorA)
        row5 = Frame(scoretable, width = 840, height = 40, bg = self.scoreboardcolorB)

        # Define top row labels
        scoretablename = Label(scoretable, text = "Name", font = (fontA, 16), fg = self.textcolorA, bg = self.dimsecondarycolor)
        scoretablepct = Label(scoretable, text = "Correct", font = (fontA, 16), fg = self.textcolorA, bg = self.dimsecondarycolor)
        scoretabledifficulty = Label(scoretable, text = "Difficulty", font = (fontA, 16), fg = self.textcolorA, bg = self.dimsecondarycolor)
        gridy = 40

        for index, value in enumerate(self.profiles):
            
            # To make rows alternative color
            if gridy == 80 or gridy == 160:
                alternating = self.scoreboardcolorA
            else:
                alternating = self.scoreboardcolorB

            # Define inner scoreboard labels
            col0 = Label(scoretable, fg = self.textcolorC, text = self.profiles[index].savename, width = 0, font = (fontA, 16), bg = alternating)
            col1 = Label(scoretable, fg = self.textcolorC, text = F"{self.profiles[index].savecorrect}0%".strip("0"), font = (fontA, 16), bg = alternating)
            col2 = Label(scoretable, fg = self.textcolorC, text = self.profiles[index].savedifficulty, font = (fontA, 16), bg = alternating)

            # Place labels
            col0.place(x = 0, y = gridy, anchor = NW)
            col1.place(x = 280, y = gridy, anchor = NW)
            col2.place(x = 560, y = gridy, anchor = NW)
            
            gridy += 40

        # Defining widgets
        replaybutton = Button(self.frame, text = "Replay", command = lambda: self.switchPage(self.difficultyPage), font = (fontA, 25), fg = self.textcolorA, bg = self.secondarycolor, borderwidth = 12)
        newplayerbutton = Button(self.frame, text = "New Player", command = lambda: self.switchPage(self.namePage), font = (fontA, 25), fg = self.textcolorA, bg = self.secondarycolor, borderwidth = 12)

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
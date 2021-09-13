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
    def difficulty (self):

        self.frame = Frame(root)
        self.frame.grid()

        title = Label(self.frame, text = "Select Difficulty").grid(row = 0, column = 1, pady = 20)
        clicktochange = Label(self.frame, text = "Click to Change").grid(row = 1, column = 1)
        difficultybutton = Button(self.frame, text = "Easy").grid(row = 2, column = 1)
        

# Gameplay Page

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
# Data Encapsulation Class
class Player:

    # Constructor
    def __init__(self, name, correct, difficulty):
        self.savename = name
        self.savecorrect = correct
        self.difficulty = difficulty

    # Display Name and High Score
    def saveprofile(self):
        
        # Format profile
        self.saveprofiletext = F"{self.savename},{self.savecorrect}0%,{self.difficulty}\n"

        # Save profile into text file
        self.savedprofiles = open('savedprofiles.txt', 'a')
        self.savedprofiles.write(self.saveprofiletext)
        self.savedprofiles.close()
        print(self.saveprofiletext)
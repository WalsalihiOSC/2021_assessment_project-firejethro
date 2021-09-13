# Data Encapsulation Class
class Player:

    # Constructor
    def __init__(self, name, correct, difficulty, age):
        self.savename = name
        self.savecorrect = correct
        self.savedifficulty = difficulty
        self.saveage = age

    # Display Name and High Score
    def saveProfile(self):
        
        # Format profile
        self.saveprofiletext = F"{self.savename},{self.savecorrect},{self.savedifficulty},{self.saveage}\n"

        # Save profile into text file
        self.savedprofiles = open('savedprofiles.txt', 'a')
        self.savedprofiles.write(self.saveprofiletext)
        self.savedprofiles.close()
        print(self.saveprofiletext)
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

    # Validate name and age
    def validate(self):  
        valid = False
        validname = False
        validage = False

        # VERIFY NAME 
        self.name_nospace = self.savename.replace(" ", "")

        # If response field is EMPTY
        if self.name_nospace == "":
            # Create and place error text under entry box
            nameerrortext = "Enter your name into the box above."

        # If name entered
        else:
            validname = True
            nameerrortext = ""

        # VERIFY AGE MODULE
        try:
            # Conversions
            self.age_nospace = self.saveage.replace(" ", "")
        
            if self.age_nospace == "":
                # Configure error text under entry box
                ageerrortext = "Enter your age into the box above."

            else:
                self.age_intnospace = int(self.age_nospace)
                if self.age_intnospace in range(5, 15):
                    ageerrortext = ""
                    validage = True
                else:
                    ageerrortext = "Enter a number between 5 and 14."
        except:
            # Configure error text under entry box
            self.ageerrorlabel = "Enter a valid number."

        if validname and validage:
            valid = True
        
        return valid, nameerrortext, ageerrortext
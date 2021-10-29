import random

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
            ageerrortext = "Enter a valid whole number."

        if validname and validage:
            valid = True
        
        # Return validity and error texts as tuple
        return valid, nameerrortext, ageerrortext

    def generateQuestion(self):
        # Set ranges based on difficulty
        # Easy
        if self.savedifficulty == "Easy":
            self.addsubmax = 100
            self.signmax = 1

        # Medium
        elif self.savedifficulty == "Medium":
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
        
        # Return values
        return self.numberone, self.numbertwo, self.sign, self.answer

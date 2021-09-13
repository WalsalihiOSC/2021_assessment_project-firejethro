# Data Encapsulation Class
class Player:

    # Constructor
    def __init__(self, n, c, qi):
        self.savename = n
        self.savecorrectresponses = c
        self.savequestionindex = qi

    # Display Name and High Score
    def displayprofile(self):
        percentage = self.savecorrectresponses / self.savequestionindex * 100
        self.newplayertext = "Name: {} | {:.2f}% Correct | {} Questions\n".format(self.savename, percentage, self.savequestionindex)
        print(self.newplayertext)

    # Records
    def saveprofile(self):
        savedplayers = open('savedplayers.txt', 'a')
        savedplayers.write(self.newplayertext)
        savedplayers.close()
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
        print("Name: {} | {:.2f}% Correct | {} Questions".format(self.savename, percentage, self.savequestionindex))
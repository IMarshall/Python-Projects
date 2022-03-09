from abc import ABC, abstractmethod

# Create variable to track score
total = 0

#Create parent class for all sports
class Sport(ABC):
    def win(self, total):
        print("You won with a total of {}!".format(total))

    # Abstract score method to allow players to score differently depending on the sport
    @abstractmethod
    def score(self, method, amount):
        pass

# Child classes with their own score methods
class Basketball(Sport):
    def score(self, amount):
        print('You shot the ball in the hoop and scored {} points!'.format(amount))
        global total
        total+= amount
        print('Your new total is {}'.format(total))

class Baseball(Sport):
    def score(self, amount):
        print('You hit a homerun and scored {} runs!'.format(amount))
        global total
        total += amount
        print('Your new total is {}'.format(total))

# Creation of player object utilizing the score(child) and win(parent) methods
Player = Basketball()
Player.score(3)
Player.win(total)


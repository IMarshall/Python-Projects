##
##
##Python 3.10.2
##
##Author: Ian Marshall
##
##Purpose: Tech Academy Python Course
##

import pygame
pygame.init()
winSound = pygame.mixer.Sound("win.wav")
loseSound = pygame.mixer.Sound("lose.wav")


def start(nice=0, mean=0, name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        check if this is a new game or not.
        if it is new, get the user's name.
        if it's not new, thank the player for playing again.
    """
    if name != "":
        print("\nThanks for playing again, ()!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, ()!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the the end of the game, your fate \nwill be sealed by your actions.")
                    stop = False

    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
        score(nice,mean,name) #pass the variables to the score()

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    #score function is being passed the values stored within the variables
    if nice >2:
        win(nice,mean,name)
    if mean >2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    pygame.mixer.Sound.play(winSound)
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (Y/N):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter (Y) for 'YES', (N) for 'NO':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    start(nice,mean,name)

def lose(nice,mean,name):
    pygame.mixer.Sound.play(loseSound)
    print("\nAh too bad, game over! \n{}, you live in a dirty beat up van down by the river, all alone!".format(name))
    again(nice,mean,name)
    


if __name__ == "__main__":
    start()

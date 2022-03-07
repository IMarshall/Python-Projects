##PARENT CLASS
class Instrument:
    name = ''
    pitch_range = ''

    ## PARENT CLASS METHOD
    def play(self):
        msg = "The {} plays some music.".format(self.name)
        return msg

##CHILD CLASSES
class Woodwind(Instrument):
    voice = 'Soprano'
    reed_size = '3'

    ##REDEFINE PARENT CLASS (POLYMORPHISM)
    def play(self):
        msg = "The {} {} goes *doot*.".format(self.voice,self.name)
        return msg

class Brass(Instrument):
    number_of_valves = 3
    mouthpiece_size = '2C'

    ##REDEFINE PARENT CLASS (POLYMORPHISM)
    def play(self):
        msg = "The {} goes *toot*".format(self.name)
        return msg

class String(Instrument):
    number_of_strings = 4
    tuning = 'GDAE'

    ##REDEFINE PARENT CLASS (POLYMORPHISM)
    def play(self):
        msg = "The {} goes *REEEEEE*".format(self.name)
        return msg

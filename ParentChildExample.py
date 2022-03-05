class Instrument:
    name = ''
    pitch_range = ''

class Woodwind(Instrument):
    voice = 'soprano'
    reed_size = '3'

class Brass(Instrument):
    number_of_valves = 3
    mouthpiece_size = '2C'

class String(Instrument):
    number_of_strings = 4
    tuning = 'GDAE'



mySentence = 'loves the color'

color_list = ['red', 'blue', 'green', 'orange']

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{} {} {}".format(name, mySentence, i)
        lst.append(msg)
    return lst

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print("You need to provide a name!")
        elif name == 'Joe':
            print("Joes aren't allowed.")
        else:
            go = False
            lst = color_function(name)
            for i in lst:
                print(i)

get_name()

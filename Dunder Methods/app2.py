import app1

def print_app2():
    name = (__name__)
    return name

if __name__ == "__main__":
    #Calls code from within this script
    print("I'm running code from {}".format(print_app2()))

    #Calls code from imported app1
    print("I'm running code from {}".format(app1.print_app()))

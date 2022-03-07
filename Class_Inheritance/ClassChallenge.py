##Class
class Driver:
    ##Define init function
    def __init__(self, name, team, nationality):
        self.name = name
        self.team = team
        self.nationality = nationality

    def information(self):
        msg = "\n{} is a {} F1 Driver for {}.".format(self.name, self.nationality, self.team)
        return msg
        
    def overtake(self):
        msg = "\nHere comes {}!!!".format(self.name)
        return msg

##Object
Seb = Driver("Sebastian Vettel", "Aston Martin", "German")


if __name__ == "__main__":
    print(Seb.information())
    print(Seb.overtake())

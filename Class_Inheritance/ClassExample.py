## PARENT CLASS
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {}\nspecies: {}\nlegs: {}\narms: {}\nDNA: {}\norigin: {}\ncarbon based: {}" \
              .format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg


## CHILD CLASS INSTANCE
class Human(Organism):
    name = "Jerry"
    species = "Homosapien"
    legs = 2
    arms = 2
    origin = "Earth"

    def joke(self):
        msg = "\nWhat's the deal with Ovaltine? It's not oval. They should call it Round-tine!"
        return msg

## ANOTHER CHILD CLASS INSTANCE
class Dog(Organism):
    name = "Spot"
    species = "Canine"
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = "Earth"

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bited it's target."
        return msg

## ANOTHER CHILD CLASS INSTANCE
class Bacterium(Organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = "Mars"

    def replication(self):
        msg = "\nThe cells begin to divide and multiply into two separate organisms!"
        return msg



if __name__ == "__main__":
    human = Human()
    print(human.information())
    print(human.joke())

    dog = Dog()
    print(dog.information())
    print(dog.bite())

    bacterium = Bacterium()
    print(bacterium.information())
    print(bacterium.replication())

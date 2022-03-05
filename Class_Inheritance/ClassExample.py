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
        msg = "\nName: {}\nspecies: {}\nlegs: {}\narms: {}\DNA: {}\norigin: {}\ncarbon based: {}" \
              .format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg








if __name__ == "__main__":
    

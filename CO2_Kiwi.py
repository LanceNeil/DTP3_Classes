class Kiwi:

    def __init__(self, nameVariable, ageVariable, ownerVariable, colourVariable):
        self.name = nameVariable
        self.age = ageVariable
        self.owner = ownerVariable
        self.colour = colourVariable

sallyTheKiwi = Kiwi("Mr.Wiggles", 13, "Lance N", "red")
hemiTheKiwi = Kiwi("hemi", 1, "Miss P", "yellow")

print("The name of the kiwi is", sallyTheKiwi.name)
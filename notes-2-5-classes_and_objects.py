# Classes and Objects

# Big Ideas:
# - Classes allow us to couple data and functions together
# - Objects ae the ACTUAL representation of the class

# Create a Pokemon class; this represents a Pokemon
class Pokemon: #use a capital letter for class name 
    def __init__(self):
        """A special method (function) called the Constructor.
        Contains all the properties/variables that describe a Pokemon"""
        self.name = ""
        self.id = 0
        self.weight = 0
        self.height = 0
        self.type = "normal"


        print ("A new Pokemon is born!")

# Create two Pokemon using our class
# Make one Pokemon that is Pikachu
pokemon_one = Pokemon ()

# Change some properties in pokemon_one
# Change its name
print(pokemon_one.name) # ""
pokemon_one.name = "Pikachu"
print(pokemon_one.name) # "Pikachu"

pokemon_one.id = 25
pokemon_one.type = "Electric"

# Make one Pokemon of your choice
pokemon_two = Pokemon()
# change its name
pokemon_two.name = "Mewtwo"
pokemon_two.id = 150
pokemon_two.type = "Psychic"
print(pokemon_two.name)
print(pokemon_two.id)
print(pokemon_two.type)
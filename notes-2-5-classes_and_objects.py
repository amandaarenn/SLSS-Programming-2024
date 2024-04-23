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
        self.actualcry = "Roooooooooar!!!"


        print ("A new Pokemon is born!")
    
    def cry(self) -> str:
        """Represents the sound a Pokemon makes
        
        Returns:
        - String representing trhe sound it makes"""
        return f'{self.name} says, "{self.actualcry}"!'

    def eat(self, food: str) -> str:
        """Represents feeding the Pokemon
        Params:
            - food: what food you feed it
        Return:
            - what it says after eating it"""
    
   
        if food.lower() == "berry":
            return f'{self.name} ate the berry and says, "YUM!"'
        elif food.lower() == "potion":
            return f"{self.name} consumed the potion and feels healthier!"
        else:
            return f"{self.name} batted the {food} away."


# Create a new child class of Pokemon
class Pikachu(Pokemon):
    def __init__ (self, name="Pikachu"):
        # Call the constructor of the parent class
        super().__init__()

        # Assign the default values to properties
        self.name = name
        self.id = 25
        self.type = "Electric"
        self.actualcry = "Pikachu"

    def thundershock(self, defender: Pokemon)->str:
        """Simulate a thundershock attack against another Pokemon.

        Params:
        - defender: defending pokemon

        Returns:
        - str representing result of attack
        """

        response = f"{self.name} used thundershock on {defender.name}!"

        if defender.type.lower() in ["Water", "flying"]:
            response = response + "It was super effective"

        return response

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

pokemon_one.actual_cry = "Pikachu!"
pokemon_two.actual_cry = "Mewtwo!"

print (pokemon_one.cry())
print (pokemon_two.cry())

# Test the eat method
print(pokemon_one.eat("berry"))
print(pokemon_one.eat("potion")) 
print(pokemon_one.eat("poison")) # mr. ubial does noy condone 
print(pokemon_two.eat("berry"))
print(pokemon_two.eat("potion"))
print(pokemon_two.eat("poison"))  # mr. ubial does not condone

pikachu_one = Pikachu()
pikachu_two = Pikachu("Speedy")

print(pikachu_one.name) #Pikachu 
print(pikachu_two.name) # Speedy
print(pikachu_one.cry())
print(pikachu_two.eat ("potion"))

print(pikachu_one.thundershock(pokemon_one))
print(pikachu_two.thundershock(pokemon_two))

# Create a new child-class of pokemon for the type of your choice
# If you don't know any pokemon, use this: https://pokemondb.net/pokedex/national
#   - create a new child class
#   - create a constructor and set the default values for its properties
#       - i.e. its name, id, type, etc.
#   - create a new method for its attack

class Sylveon(Pokemon):
    def __init__(self, name="Sylveon",):
        super().__init__()

        # Assign the default values to properties
        self.name = name
        self.id = 700
        self.type = "Fairy"
        self.actual_cry = "mefme"

    def dazzling_gleam(self, defender: Pokemon) -> str:
        """Simulate a fairy type attack"""
        
        response = f"{self.name} used dazzling gleam on {defender.name}."

        if defender.type.lower() in ["fighting", "dragon", "dark"]:
            response = response + " It was super effective!"
        
        elif defender.type.lower() in ["poison", "steel", "fire"]:
            response = response + " It was not very effective."

        return response

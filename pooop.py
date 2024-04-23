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

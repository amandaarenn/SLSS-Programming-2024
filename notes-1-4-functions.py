# Functions
# Author: Amanda
# 26th February 2024

# Create a function called say_hello
    # Its going to print "Hello"

def say_hello():
    print ("Hello!")

# Create a function called say_hello_params
# Print "Hello {parameter}!"
# --->e.g. say_hello_params("Jim")
#       >> "Hello jim!"

def say_hello_params(name):
    print (f"Hello {name}!")
    
 
say_hello()
say_hello_params("Jim")
say_hello_params("😼")

# Create a function called how_big
# It takes a number as an input/param
    # It returns how big the number is 

def how_big(num):
    if num < 0:
        return "Very small"
    if num < 10:
        return "Pretty small"
    if num <100:
        return "Small"
    if num <1000:
        return "Pretty big"
    return "Really big"

print (how_big(-1))
print (how_big(1))

result = how_big(1_000_000)
print (result)

# Create a function called adder
#   Accepts two inputs that are numbers 
#   Returnn the SUM of both numbers
def adder (x: int, y: int): 
    return x + y

result = adder (1,1)
print (result)
# Loops and Iteration
# Author: Amanda
# 5 April 2024

# Print "something" 10 times
for _ in range(10):
    print("something")

# Create a grocery list
# Do something for each item in the list
grocery_list= [
    "blueberry muffines",
    "potato chips",
    "aluminim foil",
    "orange juice",
    "RTX 4070 Super",
    "breakfast cereal",
]

# for every item in the list
#   * {grocery item}
#   * {grocery item}
#   * {grocery item}

for item in grocery_list:
    # skip the rest of the list 
    # if we get to RTX 4070
    if item == "RTX 4070 Super":
        print("Mr. Ubial can't buy a 4070")
        break # STOP LOOPING
    # print the item
    print(f"* {item}")

# Can you count using a for loop?
# Use a for loop to count to 100
for i in range(100):
    print(i + 1) 

# This loop repeats indefinitely

while True:
    print("This is an infinite loop.")   

# While loops are useful for input validation
# Askl the user if they like ice cream
# If they dont answer yes or no
# Repeat the question

user_answer = input ("Do you like ice cream")

while user_answer not in ["yes", "no", "yeah", "nah"]:
    user_answer = input ("Seriously, do you like ice cream?")

if user_answer in ["yes", "yeah"]:
    print("I LOOOOOOOVEEEE ice cream, too!")

if user_answer in  ["no", "nah"]:
    print ("how could you not like ice cream!!")
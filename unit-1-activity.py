# Unit 1 Activity
# Author: Amanda Ren
# Date: March 4th 2024

def clean_input(prompt):
    return input(prompt).strip(",.?!")
name = clean_input("What 1s your name 😼 ?")
cat = input(f"Hi, {name} I'm a cat🐈.")

cat = input("Do you l1ke cats😼? (Yes or no)")

if cat.lower() == "yes":
    print("I like cats too😻!")
    cat = input("If so what breed of cat?")
    print(f"I like {cat} cats too!!!!!!!!")

elif cat.lower() == "no":
    print("That's so rude😾!!!")

else:
    print(f"Sorry😿, 1 don't understand {cat}.")
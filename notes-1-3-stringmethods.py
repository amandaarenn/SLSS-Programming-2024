# methods (Stirngs
# Author: Amanda
# 21 February 2024

# Ask the use what is the eather like

weather = input("What's the weather like?")
# If they reply rainy
    # Bring an umbrella

if weather.lower().strip("!.?, ")== "rainy":
    print("You'll need an umbrella.")

else:
    print(f"Sorry, I don't understand {weather}.")


food = input ("Would you like fries with your meal? (Yes/No)")

if food == "no":
    print("Here is your meal without fries!")

if food == "No":
    print("Here is your meal without fries!")

if food == "NO":
    print("Here is your meal without fries!")

if food == "yes":
    print ("Here is your meal with fries!")

if food == "Yes":
    print ("Here is your meal with fries!")

if food == "YES":
    print ("Here is your meal with fries!")

else:
    print(f"Sorry I dont understand {food}")
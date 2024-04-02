# Conditionals 
# Author: Amanda Ren
# 15 February 2024

# Implement the flowchart from notes
x = 1_000_000
y = -5.7

# If x is less than y, then say so
# If x is greater than y, then say so
# If x is equal to y, then say so

# if x < y: 
#     print ("x is less than y")

# if x > y:
#     print ("x is greater then y")

# if x == y:
#     print ("x is equal to y")


# if x < y:
#     print ("x is less than y")
# elif x > y:
#     print ("x is greater than y ")
# else:
#     print("x is equal to y")

foo = int (input("Enter a number:")) # string 

if foo < -1 or int(foo) == 0:
    print("Foo is less than 1")
    print("or it's equal to zero.")

# Check if foo is inside a range
# Greater than one and less than 1000
if foo is  1 and foo < 1000:
    print ("Foo is in the range 2 - 999") 
else:
    print ("Foo is outside the range 2 - 999")
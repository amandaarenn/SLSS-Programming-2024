# Notes - Dictgionaries
# Apr 12 2024

# Big ideas:
#   - A dictionary is a data structure
#   - Dictionaries map keys to values

# Flashback to lists
person = [
    "John", "23 year old","4500 1023 2222 1111"]

# Rewrite person as a dictionary
person_dict = {
    "name": "John",
    "age": "23 years old",
    "cc num": "4500 1023 2222 1111",
    "SIN num": "700 000 000"
    }

person_one = {
    "name": "John",
    "age": "23 years old",
    "cc num": "5100 2030 3884 1992"
    }

# Get and print the persons name{?}
# print (person [0]) # Use the index

# print (person [2]) # last item in the list
# print (person [-1]) # start counting from end

# print (person [10]) # code will break

# Grab values from a dictionary
print (person_dict  ["name"])
print (person_dict ["cc num"])

# Iterate over the persons dictionary
for info in person:
    print (info)

# Iterate over the perssons list
for info in person:
    print (info)
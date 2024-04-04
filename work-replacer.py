# Emoji Replacer
# Author: Amanda
# 27 February 2024

def translate(usr_input):
    return usr_input.replace("cat", "🐈").replace("rat", "🐀")

def main():
    usr_input = input()
    print(translate(usr_input))
    
print(translate("Get to the rat"))
print(translate("I like cats."))
print(translate("I love cats and rats."))  
main()

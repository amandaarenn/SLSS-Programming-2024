# Unit 2 Activity
# Author: Amanda
# Apr 2nd 2024

def say_hello_params(name):
    print (f"Hello {name}!")

def translate(usr_input):
    return usr_input.replace("Hey Pookie", "😜😜")

def main():
    usr_input = input()
    print(translate(usr_input))

print(translate("Hey pookie!"))
main()

user_answer = input ("Do you want to go skydiving?")

while user_answer not in ["yes", "no", "yeah", "nah"]:
    user_answer = input ("Seriously, answer plz! =(")

if user_answer in ["yes", "yeah", "YES", "yes king"]:
    print("OMG REALLY LETS GOOOOO =)))")

if user_answer in  ["no", "nah"]:
    print ("how could you not wanna skydive :((((")
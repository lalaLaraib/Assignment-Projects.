"""
This program is a simple Mad Libs game where the user provides words 
that are inserted into a predefined sentence to create a fun output.

"""

start_sentence = "Code in Place is fun. I learned to program and used Python to make my"

def mad_lib():
    print("Welcome to Mad Lib Game!")
    print("Please provide the following words:")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    print(f"{start_sentence} {noun} {verb} {adjective}")
    print("Thank you for playing!")
mad_lib()    
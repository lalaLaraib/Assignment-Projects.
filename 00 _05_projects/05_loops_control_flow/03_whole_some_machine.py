"""
This program asks the user to type a given affirmation correctly.  
If the user enters it incorrectly, they are prompted to try again until they match the 
affirmation exactly.
"""

def affirmation():
    affirmation_sent = "I am capable of doing anything I put my mind to"
    user_affirmation = input(f"Please type the following affirmation:\n {affirmation_sent}: ")
    while affirmation_sent != user_affirmation:
            print("Please type the affirmation correctly.")
            user_affirmation = input(f"Hmmm That was not the affirmation. Please type the following affirmation:\n {affirmation_sent}: ")
            
    print("That's right! :)")
            
affirmation()    

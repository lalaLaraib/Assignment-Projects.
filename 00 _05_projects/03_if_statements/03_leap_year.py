"""
This program asks the user for their age and determines if they can vote  
in the fictional countries of Peturksbouipo, Stanlau, and Mayengua.
"""

Peturksbouipo = 16
Stanlau = 25
Mayengua = 48

user_input = int(input("How old are you?: "))
if user_input >= Peturksbouipo:
    print("You can vote in Peturksbouipo where the voting age is" + " "+ str(Peturksbouipo) + ".")
else:
    print("You cannot vote in Peturksbouipo Wwhere the voting age is" + " " + str(Peturksbouipo) + ".")
if user_input >= Stanlau:
    print("You can vote in Stanlau where the voting age is" + " " + str(Stanlau) + ".")
else:
    print("You cannot vote in Stanlau where the voting age is" + " " + str(Stanlau) + ".")

if user_input >= Mayengua:
    print("You can vote in Mayengua where the voting age is" + " " + str(Mayengua) + ".")
else:
    print("You cannot vote in Mayengua where the voting age is" + " " + str(Mayengua) + ".")
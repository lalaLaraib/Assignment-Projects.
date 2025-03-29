"""
This program calculates the energy equivalent of a given mass using 
Einstein’s mass-energy equivalence formula:
    E = m * c^2
"""

c = 299792458 # speed of light
def mass_energy():
    user_input = float(input("Enter the mass in kg: "))
    print("processing e = m * c^2....")
    print(f"m = {user_input} kg")
    print("c = 299792458 m/s")
    energy = user_input* c **2
    print(f"The energy equivalent of {user_input} kg is {energy} Joules.")
mass_energy()    
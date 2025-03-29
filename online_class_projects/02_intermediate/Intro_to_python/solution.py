"""
This program calculates a  weight on different planets based on Earth's gravity. 
The user inputs their weight on Earth and selects a planet, and the program computes 
the equivalent weight on the chosen planet using predefined gravity factors.
"""

MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def planetary_weight():
    earth_weight = float(input("Enter your weight on Earth: "))
    planet_name = input("Enter the name of the planet: ").lower().capitalize()

    gravity_factors = {
        "Mercury": MERCURY_GRAVITY,
        "Venus": VENUS_GRAVITY,
        "Mars": MARS_GRAVITY,
        "Jupiter": JUPITER_GRAVITY,
        "Saturn": SATURN_GRAVITY,
        "Uranus": URANUS_GRAVITY,
        "Neptune": NEPTUNE_GRAVITY
    }
    if planet_name in gravity_factors:
        planet_gravity = round(earth_weight* gravity_factors[planet_name], 2)
        print(f"The equivalent weight on {planet_name}: {planet_gravity} kg")
    else:
        print("Invalid planet name. Please enter a valid planet.")
planetary_weight()    
"""
This program is converting temperature from Fahrenheit to Celsius
based on user input.
"""

def Fahrenheit_to_Celsius():
    user_input = float(input("Enter the temperature in Fahrenheit: "))
    degrees_celsius = (user_input - 32)* 5.0/9.0
    print(f"The temperature in Celsius is {degrees_celsius:.3f}°C")
Fahrenheit_to_Celsius()
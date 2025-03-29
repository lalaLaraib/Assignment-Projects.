"""
This program calculates the total cost of fruits a user wants to buy.
It asks the user for the quantity of each fruit and sums up the total cost.
Users can press Enter without input to exit at any time.
"""

def calculate_total_cost():
    fruit_prices = {
        "apple": 5.0,
        "durian": 15.0,
        "jackfruit": 10.5,
        "kiwi": 8.0,
        "rambutan": 6.5,
        "mango": 7.5
    }

    total_cost = 0
    for fruit_name, price in fruit_prices.items():
        while True:
            try:
                user_input = input(f"Enter the quantity of {fruit_name} you want to buy (or press enter to exit): ")
                if user_input == "":
                    print("\nExiting order...\n")
                    print(f"Your total cost is ${total_cost:.2f}")
                    return
                    
                quantity = int(user_input)
                
                if quantity < 0:
                    print("Please enter a valid quantity.")
                    continue
                total_cost += quantity * price
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    print(f"Your Total cost is {total_cost:.2f}")            

calculate_total_cost()
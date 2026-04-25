
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name and not name.isdigit():  # Check if the name isn't empty and isn't a number
            return name
        else:
            print("Error: Name must be a valid string (cannot be a number).")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:  # Ensure the address isn't empty
            return address
        else:
            print("Error: Address cannot be empty.")

def pizza_list():
    num_pizzas = -1
    while (num_pizzas < 0) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input, please enter a number.')

    # Show pizza options
    print('\n== Premium Pizzas ==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    print('\n== Gourmet Pizzas ==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    # Selecting Premium Pizzas
    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input('Select Your Premium Pizza (enter the number): '))
                if 1 <= selected <= len(premium_pizzas):
                    pizza_dict['num_premium_pizzas'] += 1
                    break  # Exit the loop after a valid selection
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

    # Selecting Gourmet Pizzas
    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input('Select Your Gourmet Pizza (enter the number): '))
                if 1 <= selected <= len(gourmet_pizzas):
                    pizza_dict['num_gourmet_pizzas'] += 1
                    break  # Exit the loop after a valid selection
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

def main():
    name = customer_name()
    address = delivery_details()
    pizza_list()

    print(f"\nCustomer Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")

main()  # Start the program

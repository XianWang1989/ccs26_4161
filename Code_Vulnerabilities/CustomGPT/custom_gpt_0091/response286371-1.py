
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0,
}

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name.isalpha():  # Ensuring the input is not a number
            return name
        print("Error! Name cannot be empty and must be letters only.")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:  # If input is not empty
            return address
        print("Error! Address cannot be empty.")

def phone_number_input():
    while True:
        try:
            phone_number = int(input("Please enter your phone number (digits only): "))
            if len(str(phone_number)) >= 7:  # Checking for valid length
                return phone_number
            else:
                print("Phone number must be at least 7 digits.")
        except ValueError:
            print("Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input. Please enter a number.')

    for i, pizza in enumerate(premium_pizzas):
        print(f"{i + 1}. {pizza}")

    for i, pizza in enumerate(gourmet_pizzas):
        print(f"{i + 1}. {pizza}")

    # Select pizzas
    select_pizzas(num_pizzas)

def select_pizzas(num_pizzas):
    for _ in range(num_pizzas):
        selected = int(input("Select a pizza (1 for Premium, 2 for Gourmet): "))
        if selected in range(1, len(premium_pizzas) + 1):
            pizza_dict['num_premium_pizzas'] += 1
        elif selected in range(len(premium_pizzas) + 1, len(premium_pizzas) + len(gourmet_pizzas) + 1):
            pizza_dict['num_gourmet_pizzas'] += 1

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number_input()
    pizza_list()

    # Print receipt
    print(f"\nReceipt for {name} living at {address}. Phone: {phone}")
    print(f"Total premium pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Total gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")

main()

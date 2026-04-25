
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name and not name.isdigit():
            return name
        print("Error: Invalid input! (Cannot be a number)")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        print("Error: You must enter something!")

def phone_number_input():
    while True:
        try:
            phone_number = int(input("Please enter your phone number: "))
            if phone_number >= 1000000:  # Assuming a valid phone number is 7 digits or more
                return phone_number
        except ValueError:
            pass
        print("Phone number must be an integer with at least 7 digits.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input("How many pizzas would you like (max of 5): "))
        except ValueError:
            print("Invalid Input")

    pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, 1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):
        selected = input('Select Your Premium Pizza (or enter "next" to skip): ')
        if selected.lower() == 'next':
            break
        else:
            try:
                selected = int(selected)
                if 1 <= selected <= len(premium_pizzas):
                    pizza_dict['num_premium_pizzas'] += 1
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

    # Repeat for gourmet pizzas
    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, 1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):
        selected = input('Select Your Gourmet Pizza (or enter "next" to skip): ')
        if selected.lower() == 'next':
            break
        else:
            try:
                selected = int(selected)
                if 1 <= selected <= len(gourmet_pizzas):
                    pizza_dict['num_gourmet_pizzas'] += 1
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

    return pizza_dict

def user_info():
    while True:
        choice = input("Press 1 for delivery or 2 for pickup: ")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            pizza_list()
            break
        else:
            print("Invalid choice, please choose 1 or 2.")

# Main Execution
name = customer_name()
phone = phone_number_input()
user_info()

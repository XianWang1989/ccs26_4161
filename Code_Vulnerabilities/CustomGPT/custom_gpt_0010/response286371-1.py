
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham" , "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ")
        if not name.isalpha():  # Ensure that the name is not a numeric value
            print("Error: Name cannot be a number. Please enter a valid name.")
            name = ""
    return name  # Return the valid name

def delivery_details():
    address = ""
    while address == "":
        address = input("Please enter your delivery address: ")
    return address  # Return the valid address

def pizza_list():
    num_pizzas = -1
    while (num_pizzas < 1) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input, please enter a number between 1 and 5.')

    pizza_dict = {
        "premium_pizza_price": 8.50,
        "gourmet_pizza_price": 5.00,
        "num_premium_pizzas": 0,
        "num_gourmet_pizzas": 0
    }

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):
        # Select premium pizzas
        while True:
            selected = input('Select Your Premium Pizza (or type "next" to skip): ')
            if selected == 'next':
                break
            try:
                selected = int(selected)
                if 1 <= selected <= len(premium_pizzas):
                    pizza_dict['num_premium_pizzas'] += 1
                    print(f"You selected: {premium_pizzas[selected - 1]}")
                    break
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

        # Select gourmet pizzas
        while True:
            selected = input('Select Your Gourmet Pizza (or type "next" to skip): ')
            if selected == 'next':
                break
            try:
                selected = int(selected)
                if 1 <= selected <= len(gourmet_pizzas):
                    pizza_dict['num_gourmet_pizzas'] += 1
                    print(f"You selected: {gourmet_pizzas[selected - 1]}")
                    break
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

    return pizza_dict

def user_info():
    while True:
        choice = input("Press 1 for delivery, press 2 for pickup: ")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            break
        else:
            print("Invalid input, please enter 1 or 2.")

# Main flow
name = customer_name()
pizza_dict = pizza_list()
user_info()

# Example of printing the final receipt
print(f"\nCustomer Name: {name}")
print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")

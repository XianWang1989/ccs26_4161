
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def get_customer_name():
    while True:
        customer_name = input("Please enter your name: ")
        if customer_name.isalpha():  # Check for valid input
            return customer_name
        else:
            print("Error: You must enter a valid name (letters only).")

def get_delivery_details():
    while True:
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address:
            return delivery_address
        else:
            print("Error: You must enter something!")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number: "))
            if phone_number > 999999:  # Ensure it is a valid number
                return phone_number
            else:
                print("Error: Phone number must be 10 digits.")
        except ValueError:
            print("Error: Phone number must be an integer.")

def get_num_pizzas():
    while True:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if 0 < num_pizzas <= 5:
                return num_pizzas
            else:
                print("Invalid input, please enter a number between 1 and 5.")
        except ValueError:
            print('Invalid Input')

def pizza_list(num_pizzas):
    pizza_dict = {"num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    for _ in range(pizza_dict['num_premium_pizzas'], num_pizzas):
        selected = int(input('Select Your Premium Pizza (1 to select, 0 to skip): '))
        if selected > 0 and selected <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    for _ in range(pizza_dict['num_gourmet_pizzas'], num_pizzas):
        selected = int(input('Select Your Gourmet Pizza (1 to select, 0 to skip): '))
        if selected > 0 and selected <= len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1

    return pizza_dict

def user_info():
    while True:
        choice = input("Press 1 for delivery, Press 2 for pickup: ")
        if choice == "1":
            delivery_address = get_delivery_details()
            return "Delivery", delivery_address
        elif choice == "2":
            return "Pickup", None
        else:
            print("Invalid selection.")

def main():
    customer_name = get_customer_name()
    phone_number = get_phone_number()
    num_pizzas = get_num_pizzas()
    pizza_dict = pizza_list(num_pizzas)
    delivery_mode, delivery_address = user_info()

    # Print the receipt
    print(f"\nCustomer Name: {customer_name}")
    print(f"Phone Number: {phone_number}")
    print(f"Mode: {delivery_mode}")
    if delivery_address:
        print(f"Delivery Address: {delivery_address}")
    print(f"Total Premium Pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Total Gourmet Pizzas: {pizza_dict['num_gourmet_pizzas']}")

main()

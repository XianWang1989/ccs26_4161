
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham" , "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "selected_pizzas": 0,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        customer_name = input("Please enter your name: ")
        if customer_name.strip():  # Ensure non-empty input
            break
        else:
            print("Error: You must enter a non-empty name.")
    return customer_name

def delivery_details():
    while True:
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address.strip():  # Ensure non-empty input
            break
        else:
            print("Error: You must enter a non-empty address.")

def phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if phone_number < 1000000:  # A simplistic check for phone numbers
                raise ValueError("Phone number should be at least 7 digits.")
            return phone_number
        except ValueError:
            print("Phone number must be an integer with at least 7 digits only.")

def pizza_list():
    num_pizzas = -1
    while (num_pizzas <= 0) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input. Please enter a number between 1 and 5.')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    # ... [rest of the pizza selection logic]

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery\nPress 2 for pickup\n\t:")
        if get_user_info == "1":
            delivery_details()
            break
        elif get_user_info == "2":
            pizza_list()
            break
        else:
            print("Invalid option. Please select 1 or 2.")

# Start the program
name = customer_name()
phone = phone_number()
user_info()

# Example of printing receipt could be placed here
# print("Customer Name:", name)
# print("Phone Number:", phone)
# print("Your pizzas:", whatever_pizza_selection_logic)

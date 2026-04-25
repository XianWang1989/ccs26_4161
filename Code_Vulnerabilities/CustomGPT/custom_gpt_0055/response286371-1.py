
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

# Initialize global user info
user_info_data = {}

def customer_name():
    name = ""
    while name == "":
        try:
            name = str(input("Please enter your name: "))
        except ValueError:
            print("Error: You must enter a valid name.")
    user_info_data['name'] = name
    delivery_details()

def delivery_details():
    address = ""
    while address == "":
        try:
            address = str(input("Please enter your delivery address: "))
        except ValueError:
            print("Error: You must enter a valid address.")
    user_info_data['address'] = address
    phone_number()

def phone_number():
    phone = ""
    while len(phone) < 7 or not phone.isdigit():
        try:
            phone = input("Please enter your phone number (at least 7 digits): ")
            if len(phone) < 7:
                raise ValueError
        except ValueError:
            print("Phone number must be at least 7 digits and contain only numbers.")
    user_info_data['phone'] = phone
    pizza_list()

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if num_pizzas < 1 or num_pizzas > 5:
                raise ValueError
        except ValueError:
            print('Invalid Input, please enter a number between 1 and 5.')

    # Show pizza menu
    print('\n== Premium Pizzas ==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    print('\n== Gourmet Pizzas ==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    # Store pizza orders
    user_info_data['pizzas'] = []
    for _ in range(num_pizzas):
        selected = input('Select Your Pizza (Premium or Gourmet): ')
        user_info_data['pizzas'].append(selected)

    finalize_order()

def finalize_order():
    print("\nThank you for your order!")
    print("Your information:")
    for key, value in user_info_data.items():
        print(f"{key.capitalize()}: {value}")

# Start the program
customer_name()


premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

user_info_list = []

def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ")
        if name.isdigit():
            print("Error: Name cannot be a number.")
            name = ""
    user_info_list.append(name)
    delivery_details()

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address == "":
            print("Error: Address cannot be empty.")
    user_info_list.append(delivery_address)

    phone_number = None
    while phone_number is None or phone_number < 1000000 or phone_number > 9999999:
        try:
            phone_number = int(input("Please enter your phone number (7 digits): "))
            if phone_number < 1000000 or phone_number > 9999999:
                print("Phone number must be 7 digits.")
        except ValueError:
            print("Phone number must be an integer.")
    user_info_list.append(phone_number)

    pizza_list()

def pizza_list():
    num_pizzas = -1
    while (num_pizzas < 1) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if num_pizzas < 1 or num_pizzas > 5:
                print('Invalid Input. Enter a number between 1 and 5.')
        except ValueError:
            print('Invalid Input. Please enter a number.')

    pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    # Display pizzas
    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")
    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    # Select pizzas
    for pizza_type in ['Premium', 'Gourmet']:
        while num_pizzas > 0:
            selected = input(f'Select Your {pizza_type} Pizza (or type "next" to finish selecting): ')
            if selected.lower() == 'next':
                break
            try:
                selected = int(selected)
                if pizza_type == 'Premium':
                    if selected >= 1 and selected <= len(premium_pizzas):
                        pizza_dict['num_premium_pizzas'] += 1
                        num_pizzas -= 1
                    else:
                        print('Invalid Selection for Premium Pizza.')
                else:
                    if selected >= 1 and selected <= len(gourmet_pizzas):
                        pizza_dict['num_gourmet_pizzas'] += 1
                        num_pizzas -= 1
                    else:
                        print('Invalid Selection for Gourmet Pizza.')
            except ValueError:
                print('Invalid Input. Please enter a valid number.')

    print("Order Summary:")
    print(user_info_list)

customer_name()

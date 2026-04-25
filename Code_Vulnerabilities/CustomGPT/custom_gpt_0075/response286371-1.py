
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme",
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

# Initialize a dictionary to hold user details
user_info_dict = {}

def customer_name():
    name = ""
    while not name:
        try:
            name = input("Please enter your name: ")
            if name.isdigit():
                print("Error: Name cannot be a number.")
                name = ""
        except Exception as e:
            print("Error: " + str(e))
    return name

def delivery_details():
    address = ""
    while not address:
        try:
            address = input("Please enter your delivery address: ")
        except Exception as e:
            print("Error: " + str(e))
    return address

def phone_input():
    phone_number = ""
    while not phone_number.isdigit() or len(phone_number) < 7:
        try:
            phone_number = input("Please enter your phone number (at least 7 digits): ")
            if not phone_number.isdigit() or len(phone_number) < 7:
                print("Phone number must be at least 7 digits.")
        except Exception as e:
            print("Error: " + str(e))
    return phone_number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if num_pizzas < 1 or num_pizzas > 5:
                print('Invalid Input: Please enter a number between 1 and 5.')
        except ValueError:
            print('Invalid Input: Please enter a valid number.')

    pizza_dict = {
        "num_premium_pizzas": 0,
        "num_gourmet_pizzas": 0
    }

    # Display premium pizzas
    print('\n== Premium Pizzas ==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    # Selecting premium pizzas
    for _ in range(num_pizzas):
        selected = int(input('Select your Premium Pizza (Number): '))
        if 1 <= selected <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1
        else:
            print('Invalid Input')

    # Display gourmet pizzas
    print('\n== Gourmet Pizzas ==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):
        selected = int(input('Select your Gourmet Pizza (Number): '))
        if 1 <= selected <= len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1
        else:
            print('Invalid Input')

    return pizza_dict

# Main Program Flow
user_info_dict['name'] = customer_name()
user_info_dict['phone'] = phone_input()
user_info_dict['address'] = delivery_details()
user_info_dict['pizzas'] = pizza_list()

print("\nUser Information: ", user_info_dict)

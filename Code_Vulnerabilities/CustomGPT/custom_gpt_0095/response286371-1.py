
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

user_info_list = []

def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ")
        if name.isdigit():
            print("Error: Name cannot be a number!")
            name = ""
    user_info_list.append(name)
    delivery_details()

def delivery_details():
    address = ""
    while address == "":
        address = input("Please enter your delivery address: ")
    user_info_list.append(address)
    phone_number()

def phone_number():
    phone = ""
    while len(phone) < 7 or not phone.isdigit():
        phone = input("Please enter your phone number (at least 7 digits): ")
        if not phone.isdigit():
            print("Error: Phone number must be numeric!")
    user_info_list.append(phone)
    pizza_list()

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (1 to 5): '))
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 5.')

    pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):
        selected = input('Select Your Premium Pizza (or type "next" to skip): ')
        if selected.isdigit() and 1 <= int(selected) <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1

    for _ in range(num_pizzas):
        selected = input('Select Your Gourmet Pizza (or type "next" to skip): ')
        if selected.isdigit() and 1 <= int(selected) <= len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1

    user_info_list.append(pizza_dict)

def print_receipt():
    print("\nUser Information:")
    for info in user_info_list:
        print(info)

# Start the program
customer_name()
print_receipt()

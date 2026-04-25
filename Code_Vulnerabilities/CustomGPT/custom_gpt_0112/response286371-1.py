
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme",
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ",
    "BBQ Chicken", "Hellfire"
]

def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ")
    return name

def delivery_details():
    address = ""
    while address == "":
        address = input("Please enter your delivery address: ")
    return address

def phone_number():
    number = ""
    while len(number) < 7:
        number = input("Please enter your phone number (at least 7 digits): ")
        if not number.isdigit() or len(number) < 7:
            print("Phone number must be at least 7 digits long.")
            number = ""
    return number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    pizza_dict = {"num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    print('\n==Premium Pizzas==')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):
        selected = int(input('Select Your Premium Pizza (1-{}): '.format(len(premium_pizzas))))
        if 1 <= selected <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1

    print('\n==Gourmet Pizzas==')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):
        selected = int(input('Select Your Gourmet Pizza (1-{}): '.format(len(gourmet_pizzas))))
        if 1 <= selected <= len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1

    return pizza_dict

def user_info():
    choice = input("Press 1 for delivery, press 2 for pickup: ")
    if choice == "1":
        return delivery_details()
    elif choice == "2":
        return None

# Main Execution
name = customer_name()
phone = phone_number()
address = user_info()
pizza_orders = pizza_list()

print(f"Customer Name: {name}, Phone: {phone}, Address: {address}, Orders: {pizza_orders}")

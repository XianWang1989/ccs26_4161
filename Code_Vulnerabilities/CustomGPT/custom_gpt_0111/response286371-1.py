
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
                  "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", 
                  "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
                  "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "selected_pizzas": 0,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ")
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        delivery_address = input("Please enter your delivery address: ")
    return delivery_address

def phone_number_input():
    phone_number = ""
    while len(phone_number) < 7 or not phone_number.isdigit():
        phone_number = input("Please enter your phone number (at least 7 digits): ")
    return phone_number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for idx, pizza in enumerate(premium_pizzas):
        print(f"{idx + 1}. {pizza}")

    # Your pizza selection logic here...
    # For simplicity, I'm skipping selection logic.

def user_info():
    get_user_info = ""
    while get_user_info not in ["1", "2"]:
        get_user_info = input("Press 1 for delivery, Press 2 for pickup: ")

    if get_user_info == "1":
        delivery_details()
    elif get_user_info == "2":
        pizza_list()

# Main program execution
name = customer_name()
phone = phone_number_input()
user_info()

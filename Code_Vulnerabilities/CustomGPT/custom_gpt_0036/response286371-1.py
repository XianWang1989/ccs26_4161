
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
                  "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", 
                  "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
                  "BBQ Chicken", "Hellfire"]

pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, 
              "selected_pizzas": 0, "num_premium_pizzas": 0, 
              "num_gourmet_pizzas": 0}

def customer_name():
    name = ""
    while name == "":
        name = str(input("Please enter your name: "))
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        delivery_address = str(input("Please enter your delivery address: "))
    return delivery_address

def phone_number():
    phone = ''
    while len(phone) < 7 or not phone.isdigit():
        phone = str(input("Please enter your phone number (7 digits): "))
    return phone

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input, please enter a number between 1 and 5')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

def user_info():
    get_user_info = ""
    while get_user_info not in ["1", "2"]:
        get_user_info = str(input("Press 1 for delivery, or 2 for pickup: "))
    if get_user_info == "1":
        return delivery_details()
    elif get_user_info == "2":
        return "Pickup"

def main():
    name = customer_name()
    phone = phone_number()
    delivery_type = user_info()
    num_pizzas = pizza_list()

    print(f"\nName: {name}, Phone: {phone}, Delivery Type: {delivery_type}, Number of Pizzas: {num_pizzas}")

main()

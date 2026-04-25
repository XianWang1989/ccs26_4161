
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

def phone_number_input():
    phone_number = ""
    while not (phone_number.isdigit() and len(phone_number) >= 7):
        phone_number = input("Please enter your phone number (must be at least 7 digits): ")
    return phone_number

def pizza_list():
    num_pizzas = -1
    pizza_dict = {
        "premium_pizza_price": 8.50, 
        "gourmet_pizza_price": 5.00, 
        "num_premium_pizzas": 0, 
        "num_gourmet_pizzas": 0
    }

    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input. Please enter a number.')

    print('\n== Premium Pizzas ==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n== Gourmet Pizzas ==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    # Here you can gather the selected pizzas if needed

    return pizza_dict

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number_input()
    pizzas = pizza_list()

    # Print user information
    print(f"\nCustomer Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {phone}")

    # Further processing or receipt

main()

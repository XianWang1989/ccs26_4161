
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name.strip() != "":
            return name
        else:
            print("Error: You must enter a valid name.")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address.strip() != "":
            return address
        else:
            print("Error: You must enter a valid address.")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number (integer only): "))
            if len(str(phone)) >= 7:
                return phone
            else:
                print("Error: Phone number must be at least 7 digits.")
        except ValueError:
            print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    # Logic for selecting pizzas
    # This example omits selection logic for brevity; implement similarly to your original logic

def main():
    print("Welcome to the Pizza Ordering System!")
    name = customer_name()
    address = delivery_details()
    phone = phone_number()
    pizza_list()

    print(f"Name: {name}, Address: {address}, Phone: {phone}")

main()

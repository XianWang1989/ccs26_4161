
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

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

def phone_number():
    number = ""
    while not number.isdigit() or len(number) < 7:
        number = input("Please enter your phone number (at least 7 digits): ")
    return number

def pizza_list():
    num_pizzas = -1
    while (num_pizzas < 0) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    # Additional logic for selecting pizzas can go here

def main():
    name = customer_name()
    address = delivery_details()
    number = phone_number()
    print(f"Name: {name}, Address: {address}, Phone: {number}")
    pizza_list()

# Start the program
main()

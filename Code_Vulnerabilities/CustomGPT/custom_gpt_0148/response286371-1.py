
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

def customer_name():
    name = ""
    while name == "":
        try:
            name = input("Please enter your name: ")
            if name.isdigit():
                raise ValueError("Name cannot be a number.")
        except ValueError as e:
            print(e)
    return name

def delivery_details():
    address = ""
    while address == "":
        try:
            address = input("Please enter your delivery address: ")
        except Exception:
            print("Error: you must enter something!")
    return address

def phone_number():
    phone = -1
    while phone < 0 or len(str(phone)) < 7:
        try:
            phone = int(input("Please enter your phone number (at least 7 digits): "))
        except ValueError:
            print("Phone number must be an integer!")
    return phone

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==')
    for i, pizza in enumerate(premium_pizzas, 1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==')
    for i, pizza in enumerate(gourmet_pizzas, 1):
        print(f"{i}. {pizza}")

    # Additional logic for selecting pizzas could go here

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number()
    pizza_list()

    print(f"Customer Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {phone}")

main()

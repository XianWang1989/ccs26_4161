
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50, 
    "gourmet_pizza_price": 5.00, 
    "selected_pizzas": 0, 
    "num_premium_pizzas": 0, 
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if not name.strip():
                raise ValueError("Name cannot be empty.")
            return name
        except ValueError as e:
            print(e)

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if not address.strip():
                raise ValueError("Address cannot be empty.")
            return address
        except ValueError as e:
            print(e)

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number (must be a number): "))
            if phone < 1000000:  # Suppose you want at least 7 digits
                raise ValueError("Phone number must be at least 7 digits.")
            return phone
        except ValueError as e:
            print(e)

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if num_pizzas < 1:
                raise ValueError("You must order at least one pizza.")
        except ValueError as e:
            print(e)

    for idx, pizza in enumerate(premium_pizzas, start=1):
        print(f"{idx}. {pizza}")

    for idx, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{idx + len(premium_pizzas)}. {pizza}")

    # Handle pizza selection here if needed...
    # This part can be added after the descriptions.

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number()
    pizza_list()

    print(f"\nCustomer Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {phone}")

main()

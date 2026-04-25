
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
        try:
            name = input("Please enter your name: ")
            if not name.isdigit() and name.strip() != "":
                return name
            else:
                print("Error: name cannot be numeric or empty.")
        except Exception as e:
            print(f"Error: {e}")

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address.strip() != "":
                return address
            else:
                print("Error: address cannot be empty.")
        except Exception as e:
            print(f"Error: {e}")

def pizza_list():
    num_pizzas = -1
    while (num_pizzas < 0) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input, please enter a number between 1 and 5.')

    for i, pizza in enumerate(premium_pizzas):
        print(f"{i + 1}. {pizza}")

    for i, pizza in enumerate(gourmet_pizzas):
        print(f"{i + 1}. {pizza}")

    return num_pizzas

def user_info():
    while True:
        choice = input("Press 1 for delivery or 2 for pickup: ")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            print("Pickup selected.")
            break
        else:
            print("Invalid input, please choose 1 or 2.")

# Main flow
name = customer_name()
print(f"Customer Name: {name}")
num_pizzas = pizza_list()
user_info()

# Final output can be managed here as needed

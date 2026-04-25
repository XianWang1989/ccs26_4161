
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
        try:
            name = str(input("Please enter your name: "))
            return name  # Return the name to use later
        except ValueError:
            print("Error: you must enter a valid name!")

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = str(input("Please enter your delivery address: "))
            return delivery_address  # Return the address to use later
        except ValueError:
            print("Error: you must enter a valid address!")

def phone_number():
    number = -1
    while number < 0 or number < 7:
        try:
            number = int(input("Please enter your phone number:\n\t"))
            return number  # Return the phone number to use later
        except ValueError:
            print("Phone number must be an integer only (no letters).")

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    selected_pizzas = []
    for _ in range(num_pizzas):
        selected = int(input('Select Your Premium Pizza (or enter 0 for none): '))
        if selected > 0 and selected <= len(premium_pizzas):
            selected_pizzas.append(premium_pizzas[selected - 1])

    return selected_pizzas  # Return selected pizzas to use later

def user_info():
    choice = ""
    while choice not in ["1", "2"]:
        choice = str(input("Press 1 for delivery, or 2 for pickup: "))
        if choice == "1":
            delivery_details()
        elif choice == "2":
            pizza_list()

# Main program execution
name = customer_name()
phone = phone_number()
selected_pizzas = pizza_list()
print(f"Customer Name: {name}, Phone Number: {phone}, Selected Pizzas: {selected_pizzas}")

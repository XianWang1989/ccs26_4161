
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", 
                  "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]
pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, 
              "selected_pizzas": 0, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

def customer_name():
    name = ""
    while name == "":
        try:
            name = str(input("Please enter your name: "))
        except ValueError:
            print("Error: You must enter a valid name.")
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = str(input("Please enter your delivery address: "))
        except ValueError:
            print("Error: You must enter a valid address.")
    return delivery_address

def phone_number():
    number = -1
    while number < 0 or number < 7:
        try:
            number = int(input("Please enter your phone number (numeric only): "))
        except ValueError:
            print("Phone number must be an integer only.")
    return number

def pizza_list():
    num_pizzas = -1
    while (num_pizzas <= 0) or (num_pizzas > 5):
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

    # Continue your selection logic for pizzas...

def user_info():
    while True:
        get_user_info = str(input("Press 1 for delivery or 2 for pickup: "))
        if get_user_info == "1":
            delivery_details()
            break
        elif get_user_info == "2":
            pizza_list()
            break

# Main program flow
name = customer_name()
print(f"Customer Name: {name}")
number = phone_number()
print(f"Phone Number: {number}")
user_info()

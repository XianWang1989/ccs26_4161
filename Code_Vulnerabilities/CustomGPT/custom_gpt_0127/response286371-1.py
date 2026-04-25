
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
    while True:
        try:
            name = input("Please enter your name: ")
            if not name.isalpha():
                raise ValueError("Name must not contain numbers")
            return name
        except ValueError as e:
            print("Error:", e)

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        else:
            print("Error: You must enter something!")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number (digits only): "))
            if phone_number < 1000000:  # Example check for realistic phone number length
                raise ValueError("Invalid phone number")
            return phone_number
        except ValueError as e:
            print("Error:", e)

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if num_pizzas < 1 or num_pizzas > 5:
                raise ValueError("Invalid input, try again.")
        except ValueError as e:
            print(e)

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    return num_pizzas

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery or 2 for pickup: ")
        if get_user_info == "1":
            delivery_details()
            break
        elif get_user_info == "2":
            pizza_list()
            break
        else:
            print("Invalid input, try again.")

# Main execution flow
name = customer_name()
phone = get_phone_number()  # Get phone number
user_info()  # Get user information and proceed with order


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
            name = input("Please enter your name: ")
            if name.isdigit():
                raise ValueError("Name cannot be a number!")
        except ValueError as e:
            print(e)
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = input("Please enter your delivery address: ")
        except:
            print("Error: You must enter something!")

    return delivery_address

def get_phone_number():
    phone_number = ""
    while not phone_number.isdigit() or len(phone_number) < 7:
        try:
            phone_number = input("Please enter your phone number:\n\t")
            if not phone_number.isdigit():
                raise ValueError("Phone number must be integer only.")
        except ValueError as e:
            print(e)
    return phone_number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas):
        print(f"{i + 1}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas):
        print(f"{i + 1}. {pizza}")

    # Add pizza selection logic here...
    return num_pizzas

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery\nPress 2 for pickup\n\t: ")
        if get_user_info == "1":
            delivery_details()
            break
        elif get_user_info == "2":
            pizza_list()
            break

# Main Execution
name = customer_name()
phone_number = get_phone_number()
user_info()

# Output
print(f"Customer Name: {name}")
print(f"Phone Number: {phone_number}")

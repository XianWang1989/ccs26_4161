
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

user_data = {}

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.strip() == "":
                raise ValueError("Name cannot be empty.")
            user_data['customer_name'] = name
            break
        except ValueError as e:
            print(e)

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address.strip() == "":
                raise ValueError("Address cannot be empty.")
            user_data['delivery_address'] = address
            break
        except ValueError as e:
            print(e)

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number (digits only): "))
            if phone < 1000000:  # simple check for size
                raise ValueError("Phone number is too short.")
            user_data['phone_number'] = phone
            break
        except ValueError as e:
            print(e)

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if num_pizzas <= 0:
                raise ValueError("Please order at least 1 pizza.")
        except ValueError as e:
            print(e)

    user_data['num_pizzas'] = num_pizzas
    print_pizza_options()

def print_pizza_options():
    print('\n==Premium Pizzas==')
    for i, pizza in enumerate(premium_pizzas, 1):
        print(f'{i}. {pizza}')
    print('\n==Gourmet Pizzas==')
    for i, pizza in enumerate(gourmet_pizzas, 1):
        print(f'{i}. {pizza}')

def gather_user_info():
    customer_name()
    phone_number()
    delivery_details()
    pizza_list()

gather_user_info()
print("User Information:", user_data)

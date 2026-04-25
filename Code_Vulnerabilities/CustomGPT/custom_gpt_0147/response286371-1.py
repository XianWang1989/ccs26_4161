
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
    while True:  # Continue until a valid name is provided
        customer_name = input("Please enter your name: ")
        if customer_name:  # Ensure name is not empty
            return customer_name  # Return the name after valid input

def delivery_details():
    while True:  # Continue until a valid address is provided
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address:  # Ensure address is not empty
            return delivery_address  # Return the address after valid input

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number: "))
            if phone_number >= 0:
                return phone_number
        except ValueError:
            print("Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    # The next sections that list pizzas will remain the same
    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    selected_premium = []
    selected_gourmet = []

    # Selecting premium pizzas
    while len(selected_premium) < num_pizzas:
        try:
            selected = int(input('Select Your Premium Pizza (1-{0}): '.format(len(premium_pizzas))))
            if selected in range(1, len(premium_pizzas) + 1):
                selected_premium.append(premium_pizzas[selected - 1])
        except ValueError:
            print('Invalid Input')

    # Selecting gourmet pizzas (same logic)
    while len(selected_gourmet) < num_pizzas:
        try:
            selected = int(input('Select Your Gourmet Pizza (1-{0}): '.format(len(gourmet_pizzas))))
            if selected in range(1, len(gourmet_pizzas) + 1):
                selected_gourmet.append(gourmet_pizzas[selected - 1])
        except ValueError:
            print('Invalid Input')

    return selected_premium, selected_gourmet

def user_info():
    get_user_info = input("Press 1 for delivery or Press 2 for pickup: ")
    if get_user_info == "1":
        delivery_address = delivery_details()
    elif get_user_info == "2":
        delivery_address = ""
    return customer_name(), get_phone_number(), delivery_address

# Begin program
customer, phone, address = user_info()
premium, gourmet = pizza_list()

print(f"Customer: {customer}, Phone: {phone}, Address: {address}")
print(f"Selected Premium Pizzas: {premium}, Selected Gourmet Pizzas: {gourmet}")

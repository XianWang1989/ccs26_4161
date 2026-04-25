
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
                  "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]

gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

num_pizzas = -1
user_recipt = {}

def customer_name():
    name = ""
    while name == "":
        try:
            name = str(input("Please enter your name: "))
        except:
            print("Error: you must enter something!")
    user_recipt['name'] = name  # store the name for later
    return delivery_details()

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = str(input("Please enter your delivery address: "))
        except:
            print("Error: you must enter something!")
    user_recipt['delivery_address'] = delivery_address  # store the address
    return phone_number()

def phone_number():
    phone_number = ""
    while not (phone_number.isdigit() and 7 <= len(phone_number) <= 15):  # Validate phone length
        try:
            phone_number = input("Please enter your phone number (7 to 15 digits long): ")
            if not (phone_number.isdigit() and 7 <= len(phone_number) <= 15):
                raise ValueError("Invalid format")
        except:
            print("Phone number must be digits only and between 7 to 15 characters long.")
    user_recipt['phone_number'] = phone_number  # store the number
    return pizza_list()

def pizza_list():
    num_pizzas = -1
    while (num_pizzas <= 0) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except:
            print('Invalid Input')

    pizza_dict = {
        "premium_pizza_price": 8.50, 
        "gourmet_pizza_price": 5.00,
        "num_premium_pizzas": 0, 
        "num_gourmet_pizzas": 0
    }

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(str(i + 1) + '. ' + premium_pizzas[i])

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(str(i + 1) + '. ' + gourmet_pizzas[i])

    for _ in range(num_pizzas):
        selected = input('Select Your Premium Pizza (or type "next" to skip): ')
        if selected.lower() == 'next': 
            break
        selected = int(selected)
        if selected > 0 and selected <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1

    for _ in range(num_pizzas):
        selected = input('Select Your Gourmet Pizza (or type "next" to skip): ')
        if selected.lower() == 'next': 
            break
        selected = int(selected)
        if selected > 0 and selected <= len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1

    # Print Receipt
    print_receipt(user_recipt, pizza_dict)

def print_receipt(user_recipt, pizza_dict):
    print("== Your Order Receipt ==")
    print("Name:", user_recipt['name'])
    print("Address:", user_recipt['delivery_address'])
    print("Phone:", user_recipt['phone_number'])
    print('Total number of premium pizzas:', pizza_dict['num_premium_pizzas'])
    print('Total number of gourmet pizzas:', pizza_dict['num_gourmet_pizzas'])
    total_cost = (pizza_dict["num_premium_pizzas"] * pizza_dict['premium_pizza_price'] +
                  pizza_dict["num_gourmet_pizzas"] * pizza_dict['gourmet_pizza_price'])
    print('Total cost: $' + str(round(total_cost, 2)))

# Start the customer order process
customer_name()

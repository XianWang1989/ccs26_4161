premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham" , "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "selected_pizzas": 0,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

# Define all your functions first
def customer_name():
    name = ""
    while name == "":
        try:
            name = input("Please enter your name: ")
            if name.isdigit():
                print("Name cannot be a number!")
                name = ""
        except:
            print("Error: Please enter something!")
    user_info(name)

def delivery_details():
    address = ""
    phone_number = ""
    while address == "":
        try:
            address = input("Please enter your delivery address: ")
        except:
            print("Error: You must enter something!")

    while not (phone_number.isdigit() and len(phone_number) >= 7):
        try:
            phone_number = input("Please enter your phone number: ")
            if not phone_number.isdigit():
                raise ValueError
        except:
            print("Phone number must be digits only and at least 7 digits long.")
    return address, phone_number

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i+1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i+1}. {gourmet_pizzas[i]}")

    while num_pizzas > 0:
        selected = input('Select Your Premium Pizza (enter number or "next"): ')
        if selected == 'next':
            break
        if selected.isdigit() and 0 < int(selected) <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1
            num_pizzas -= 1
        else:
            print('Invalid input.')

    while num_pizzas > 0:
        selected = input('Select Your Gourmet Pizza (enter number or "next"): ')
        if selected == 'next':
            break
        if selected.isdigit() and 0 < int(selected) <= len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1
            num_pizzas -= 1
        else:
            print('Invalid input.')

def user_info(name):
    choice = ""
    while choice not in ["1", "2"]:
        choice = input("Press 1 for delivery, 2 for pickup: ")
    if choice == "1":
        address, phone = delivery_details()
    else:
        address, phone = "N/A (Pickup)", "N/A"

    pizza_list()
    print_receipt(name, address, phone)

def print_receipt(name, address, phone):
    print("\n===== Receipt =====")
    print("Customer Name:", name)
    print("Address:", address)
    print("Phone Number:", phone)
    print('Total premium pizzas:', pizza_dict['num_premium_pizzas'])
    print('Total gourmet pizzas:', pizza_dict['num_gourmet_pizzas'])
    cost = (
        pizza_dict["num_premium_pizzas"] * pizza_dict['premium_pizza_price'] +
        pizza_dict["num_gourmet_pizzas"] * pizza_dict['gourmet_pizza_price']
    )
    print('Total cost: $' + str(round(cost, 2)))

# Start the program
customer_name()

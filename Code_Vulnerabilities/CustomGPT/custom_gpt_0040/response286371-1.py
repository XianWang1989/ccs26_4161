
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0,
    "num_pizzas": 0
}

def user_info():
    while True:
        get_user_info = str(input("Press 1 for delivery, Press 2 for pickup: "))
        if get_user_info == "1":
            delivery_details()
            break
        elif get_user_info == "2":
            pizza_list()
            break

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name.strip() == "":
            print("Error: You must enter something!")
        else:
            print(f"Welcome, {name}!")
            return name

def delivery_details():
    address = ""
    while address == "":
        address = input("Please enter your delivery address: ")
        if address.strip() == "":
            print("Error: You must enter something!")

def phone_number_input():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if len(str(phone_number)) < 7:
                print("Phone number must be at least 7 digits.")
            else:
                return phone_number
        except ValueError:
            print("Phone number must be an integer only.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n== Premium Pizzas ==\n')
    for index, pizza in enumerate(premium_pizzas, start=1):
        print(f"{index}. {pizza}")

    print('\n== Gourmet Pizzas ==\n')
    for index, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{index}. {pizza}")

    # Selecting pizzas
    for _ in range(num_pizzas):
        selected = int(input('Select Your Premium Pizza (1 to 7): '))
        if 1 <= selected <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1

        selected = int(input('Select Your Gourmet Pizza (1 to 5): '))
        if 1 <= selected <= len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1

# Main execution starts here
name = customer_name()
phone = phone_number_input()
user_info()

# Print out your receipt information (can add more details as needed)
print(f"\nReceipt: {pizza_dict['num_premium_pizzas']} premium pizzas, {pizza_dict['num_gourmet_pizzas']} gourmet pizzas.")

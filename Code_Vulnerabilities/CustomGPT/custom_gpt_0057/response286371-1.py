
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "selected_pizzas": 0, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

def customer_name():
    name = ""
    while name == "":
        try:
            name = str(input("Please enter your name: "))
        except:
            print("Error! You must enter something!")
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = str(input("Please enter your delivery address: "))
        except:
            print("Error! You must enter something!")

def phone_number():
    number = 0
    while number < 1000000 or number > 9999999:
        try:
            number = int(input("Please enter your phone number (7 digits): "))
        except:
            print("Phone number must be a 7-digit integer!")
    return number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except:
            print('Invalid Input')

    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    selected_premium = 0
    selected_gourmet = 0

    while selected_premium < num_pizzas:
        selected = input('Select Your Premium Pizza (or type "next" to end): ')
        if selected.lower() == 'next':
            break
        try:
            selected = int(selected)
            if 1 <= selected <= len(premium_pizzas):
                selected_premium += 1
                pizza_dict['num_premium_pizzas'] += 1
            else:
                print('Invalid Input')
        except:
            print('Invalid Input')

    while selected_gourmet < num_pizzas - selected_premium:
        selected = input('Select Your Gourmet Pizza (or type "next" to end): ')
        if selected.lower() == 'next':
            break
        try:
            selected = int(selected)
            if 1 <= selected <= len(gourmet_pizzas):
                selected_gourmet += 1
                pizza_dict['num_gourmet_pizzas'] += 1
            else:
                print('Invalid Input')
        except:
            print('Invalid Input')

def user_info():
    while True:
        choice = input("Press 1 for delivery, Press 2 for pickup: ")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            pizza_list()
            break

name = customer_name()
number = phone_number()
user_info()

print(f"\nCustomer Name: {name}, Phone Number: {number}")
print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")

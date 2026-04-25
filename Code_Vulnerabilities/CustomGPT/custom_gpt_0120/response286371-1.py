
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

# Global variables to store user information
customer_name_info = ""
delivery_address_info = ""
phone_number_info = 0
num_pizzas_info = 0

def customer_name():
    global customer_name_info
    while customer_name_info == "":
        try:
            customer_name_info = str(input("Please enter your name: "))
            if customer_name_info.isdigit():
                raise ValueError("Name cannot be a number.")
        except ValueError as e:
            print(e)

def delivery_details():
    global delivery_address_info
    while delivery_address_info == "":
        try:
            delivery_address_info = str(input("Please enter your delivery address: "))
        except:
            print("Error: You must enter something!")

def phone_number():
    global phone_number_info
    while phone_number_info <= 0 or phone_number_info < 7:
        try:
            phone_number_info = int(input("Please enter your phone number:\n\t"))
            if phone_number_info < 1000000:  # Ensure it's a valid phone number
                print("Phone number must be at least 7 digits.")
                phone_number_info = 0
        except ValueError:
            print("Phone number must be an integer only.")

def pizza_list():
    global num_pizzas_info
    while (num_pizzas_info <= 0) or (num_pizzas_info > 5):
        try:
            num_pizzas_info = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    pizza_dict = {
        "premium_pizza_price": 8.50,
        "gourmet_pizza_price": 5.00,
        "num_premium_pizzas": 0,
        "num_gourmet_pizzas": 0
    }

    print('\n==Premium Pizzas==')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    while True:
        if num_pizzas_info == 0:
            break
        selected = input('Select Your Premium Pizza (or type "next" to move on): ')
        if selected == 'next':
            break
        try:
            selected = int(selected)
            if selected > 0 and selected <= len(premium_pizzas):
                pizza_dict['num_premium_pizzas'] += 1
                num_pizzas_info -= 1
            else:
                print('Invalid Input')
        except ValueError:
            print('Invalid Input')

    while True:
        if num_pizzas_info == 0:
            break
        selected = input('Select Your Gourmet Pizza (or type "next" to finish): ')
        if selected == 'next':
            break
        try:
            selected = int(selected)
            if selected > 0 and selected <= len(gourmet_pizzas):
                pizza_dict['num_gourmet_pizzas'] += 1
                num_pizzas_info -= 1
            else:
                print('Invalid Input')
        except ValueError:
            print('Invalid Input')

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery or 2 for pickup:\n\t")
        if get_user_info == "1":
            delivery_details()
            break
        elif get_user_info == "2":
            pizza_list()
            break

# Main program flow
customer_name()
phone_number()
user_info()

# Print collected information
print(f"\nCustomer Name: {customer_name_info}")
print(f"Phone Number: {phone_number_info}")
print(f"Delivery Address: {delivery_address_info}")

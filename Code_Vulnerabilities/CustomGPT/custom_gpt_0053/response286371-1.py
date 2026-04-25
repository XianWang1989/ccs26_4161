
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
    "BBQ Chicken", "Hellfire"
]

pizza_dict = {
    "premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00,
    "selected_pizzas": 0, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        customer_name = input("Please enter your name: ")
        if customer_name:
            return customer_name
        else:
            print("Error: You must enter something! (Cannot be a number)")

def delivery_details():
    while True:
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address:
            return delivery_address
        else:
            print("Error: You must enter something!")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number (digits only): "))
            if len(str(phone)) >= 7: # Ensure phone number length is valid
                return phone
        except ValueError:
            print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input: Must be an integer.')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    selected_pizzas = []

    while num_pizzas > 0:
        selected = input('Select Your Pizza (or type "next" to finish): ')
        if selected.lower() == 'next':
            break
        try:
            selected = int(selected)
            if 1 <= selected <= len(premium_pizzas):
                selected_pizzas.append(premium_pizzas[selected - 1])
                num_pizzas -= 1
            else:
                print('Invalid Input: Select a valid pizza number.')
        except ValueError:
            print('Invalid Input: Must be an integer.')

    return selected_pizzas

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery, press 2 for pickup: ")
        if get_user_info == "1":
            delivery = delivery_details()
            return delivery
        elif get_user_info == "2":
            return None

# Main Program
name = customer_name()
phone = phone_number()
orders = pizza_list()
delivery_address = user_info()

# Final Output
receipt = {
    "name": name,
    "phone": phone,
    "delivery_address": delivery_address,
    "ordered_pizzas": orders
}

print("\nReceipt:")
for key, value in receipt.items():
    print(f"{key}: {value}")

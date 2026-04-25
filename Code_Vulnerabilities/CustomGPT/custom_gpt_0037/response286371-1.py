
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
        name = input("Please enter your name: ")
        if name:
            return name
        print("Error: You must enter a name!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        print("Error: You must enter an address!")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if len(str(phone_number)) >= 7:
                return phone_number
            else:
                print("Phone number must be at least 7 digits.")
        except ValueError:
            print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for index, pizza in enumerate(premium_pizzas, start=1):
        print(f"{index}. {pizza}")

    for index, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{index + len(premium_pizzas)}. {pizza}")

    # Select pizzas
    for _ in range(num_pizzas):
        while True:
            selected = input('Select your pizza (1 for Premium, 2 for Gourmet) or type "next" to proceed: ')
            if selected == 'next':
                break
            else:
                try:
                    selected = int(selected)
                    if selected <= len(premium_pizzas):
                        pizza_dict['num_premium_pizzas'] += 1
                    elif selected <= len(premium_pizzas) + len(gourmet_pizzas):
                        pizza_dict['num_gourmet_pizzas'] += 1
                    else:
                        print('Invalid selection. Try again.')
                except ValueError:
                    print('Invalid input. Please enter a number.')

def main():
    name = customer_name()
    address = delivery_details()
    phone_number = get_phone_number()
    pizza_list()

    # Print user info at the end
    print(f"\nCustomer Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {phone_number}")
    print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")

main()

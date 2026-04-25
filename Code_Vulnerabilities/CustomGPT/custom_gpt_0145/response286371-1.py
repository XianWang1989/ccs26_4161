
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name:
            return name
        else:
            print("Error: You must enter a name!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        else:
            print("Error: You must enter a delivery address!")

def phone_number_input():
    while True:
        try:
            phone_number = int(input("Please enter your phone number (digits only): "))
            if len(str(phone_number)) >= 7:  # Ensure the phone number is valid
                return phone_number
            else:
                print("Phone number must be at least 7 digits.")
        except ValueError:
            print("Invalid input. Please enter digits only.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):
        selected = int(input('Select Your Premium Pizza (1-{}): '.format(len(premium_pizzas))))
        if 1 <= selected <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1

    for _ in range(num_pizzas):
        selected = int(input('Select Your Gourmet Pizza (1-{}): '.format(len(gourmet_pizzas))))
        if 1 <= selected <= len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1

    return pizza_dict

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number_input()
    pizzas = pizza_list()

    # Print out all collected information
    print(f"\nCustomer Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {phone}")
    print(f"Number of Premium Pizzas: {pizzas['num_premium_pizzas']}")
    print(f"Number of Gourmet Pizzas: {pizzas['num_gourmet_pizzas']}")

main()

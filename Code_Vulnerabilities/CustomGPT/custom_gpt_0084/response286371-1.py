
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

def customer_name():
    name = ""
    while name == "":
        try:
            name = str(input("Please enter your name: "))
        except ValueError:
            print("Error: You must enter a valid name.")
    return name

def delivery_details():
    address = ""
    while address == "":
        try:
            address = str(input("Please enter your delivery address: "))
        except ValueError:
            print("Error: You must enter a valid address.")
    return address

def phone_number():
    phone = -1
    while phone < 0:
        try:
            phone = int(input("Please enter your phone number: "))
            if len(str(phone)) < 7:
                print("Phone number must be at least 7 digits.")
                phone = -1
        except ValueError:
            print("Phone number must be an integer only.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input.')

    # Selecting premium pizzas
    for _ in range(num_pizzas):
        selected = -1
        while selected < 1 or selected > len(premium_pizzas):
            try:
                selected = int(input('Select Your Premium Pizza (1 to {}): '.format(len(premium_pizzas))))
                if selected > 0:
                    pizza_dict['num_premium_pizzas'] += 1
            except ValueError:
                print('Invalid input.')

    # Selecting gourmet pizzas
    for _ in range(num_pizzas):
        selected = -1
        while selected < 1 or selected > len(gourmet_pizzas):
            try:
                selected = int(input('Select Your Gourmet Pizza (1 to {}): '.format(len(gourmet_pizzas))))
                if selected > 0:
                    pizza_dict['num_gourmet_pizzas'] += 1
            except ValueError:
                print('Invalid input.')

def main():
    name = customer_name()
    delivery_address = delivery_details()
    phone_number()  # gather phone number
    pizza_list()  # gather pizza orders

    print("\nReceipt:")
    print(f"Name: {name}")
    print(f"Delivery Address: {delivery_address}")
    print(f"Total Premium Pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Total Gourmet Pizzas: {pizza_dict['num_gourmet_pizzas']}")

main()

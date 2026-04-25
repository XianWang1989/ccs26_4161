
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

# Global variables
user_info_list = []

def customer_name():
    name = ""
    while name == "":
        try:
            name = str(input("Please enter your name: "))
        except ValueError:
            print("Error: You must enter something! (cannot be a number)")

    user_info_list.append(name)  # Store customer name
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = str(input("Please enter your delivery address: "))
        except ValueError:
            print("Error: You must enter something!")

    user_info_list.append(delivery_address)  # Store delivery address
    return delivery_address

def collect_phone_number():
    phone_number = ""
    while len(phone_number) < 7 or not phone_number.isdigit():
        phone_number = input("Please enter your phone number (at least 7 digits): ")
        if not phone_number.isdigit() or len(phone_number) < 7:
            print("Phone number must be at least 7 digits long and contain only numbers.")

    user_info_list.append(phone_number)  # Store phone number
    return phone_number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input. Please enter a number between 1 and 5.')

    pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    # Select pizzas
    for _ in range(num_pizzas):
        selected = 0
        while selected <= 0 or selected > len(premium_pizzas):
            try:
                selected = int(input('Select Your Premium Pizza (1 to {}): '.format(len(premium_pizzas))))
                if selected <= 0 or selected > len(premium_pizzas):
                    print('Invalid Input')
                else:
                    pizza_dict['num_premium_pizzas'] += 1
            except ValueError:
                print('Invalid Input')

    # Gourmet Pizza selection would be similar...

def main():
    customer_name()
    collect_phone_number()
    delivery_details()
    pizza_list()

    # Print all collected info
    print("\nUser Information:")
    print(user_info_list)

# Start the program
main()

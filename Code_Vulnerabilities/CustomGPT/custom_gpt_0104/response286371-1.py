
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

user_info_list = []

def customer_name():
    while True:
        name = input("Please enter your name: ").strip()
        if name:
            user_info_list.append(name)
            break
        else:
            print("Error: You must enter a valid name!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ").strip()
        if address:
            user_info_list.append(address)
            break
        else:
            print("Error: You must enter a valid address!")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number:\n\t"))
            if len(str(phone)) >= 7:  # Ensure it is a valid length
                user_info_list.append(phone)
                break
            else:
                print("Error: Phone number must be at least 7 digits.")
        except ValueError:
            print("Phone number must be an integer only.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input, please enter a number between 1 and 5.')

    pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    # Display premium pizzas
    print('\n== Premium Pizzas ==\n')
    for i, pizza in enumerate(premium_pizzas):
        print(f"{i + 1}. {pizza}")

    # Code for selecting premium pizzas
    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input('Select Your Premium Pizza: '))
                if 1 <= selected <= len(premium_pizzas):
                    pizza_dict['num_premium_pizzas'] += 1
                    break
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

    # Display gourmet pizzas
    print('\n== Gourmet Pizzas ==\n')
    for i, pizza in enumerate(gourmet_pizzas):
        print(f"{i + 1}. {pizza}")

    # Code for selecting gourmet pizzas
    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input('Select Your Gourmet Pizza: '))
                if 1 <= selected <= len(gourmet_pizzas):
                    pizza_dict['num_gourmet_pizzas'] += 1
                    break
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

def main():
    customer_name()
    phone_number()
    delivery_details()
    pizza_list()

    print("\nUser Info Summary:")
    for info in user_info_list:
        print(info)

# Start the program
main()

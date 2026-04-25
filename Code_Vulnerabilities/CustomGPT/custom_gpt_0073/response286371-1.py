
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

user_info_list = []

def customer_name():
    name = ""
    while name == "":
        try:
            name = input("Please enter your name: ")
            if name.isdigit():
                raise ValueError("Name cannot be a number.")
        except ValueError as e:
            print(e)
    user_info_list.append(name)
    delivery_details()


def delivery_details():
    address = ""
    while address == "":
        try:
            address = input("Please enter your delivery address: ")
        except:
            print("Error: you must enter something!")
    user_info_list.append(address)
    phone_number()


def phone_number():
    phone = ""
    while not phone.isdigit() or len(phone) < 7:
        try:
            phone = input("Please enter your phone number (7 digits minimum): ")
            if not phone.isdigit():
                raise ValueError("Phone number must be digits only.")
        except ValueError as e:
            print(e)
    user_info_list.append(phone)
    pizza_list()


def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except:
            print('Invalid Input, please enter a number.')

    pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i+1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i+1}. {gourmet_pizzas[i]}")

    while num_pizzas > 0:
        try:
            selected = int(input('Select your pizza (by number) or enter 0 to finish: '))
            if selected == 0:
                break
            if selected <= 0 or selected > len(premium_pizzas) + len(gourmet_pizzas):
                print('Invalid Input')
            elif selected <= len(premium_pizzas):
                pizza_dict['num_premium_pizzas'] += 1
                num_pizzas -= 1
            else:
                pizza_dict['num_gourmet_pizzas'] += 1
                num_pizzas -= 1
        except ValueError:
            print('Invalid Input')

    print_receipt(pizza_dict)

def print_receipt(pizza_dict):
    print("\n== Receipt ==")
    print("User Information:")
    print(user_info_list)
    print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")
    cost = (pizza_dict["num_premium_pizzas"] * pizza_dict['premium_pizza_price']) + (pizza_dict["num_gourmet_pizzas"] * pizza_dict['gourmet_pizza_price'])
    print(f'Total cost: ${cost:.2f}')

# Start the program
customer_name()

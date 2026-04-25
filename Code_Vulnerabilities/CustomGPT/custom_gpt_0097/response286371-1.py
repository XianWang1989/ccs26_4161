
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.strip() == "":
                raise ValueError
            return name
        except ValueError:
            print("Error: You must enter a valid name!")

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address.strip() == "":
                raise ValueError
            return address
        except ValueError:
            print("Error: You must enter a valid address!")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if phone_number < 1000000:  # Ensure it's a valid phone number format
                raise ValueError
            return phone_number
        except ValueError:
            print("Phone number must be an integer and valid!")

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00,
                   "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    while num_pizzas > 0:
        selected = input('Select Your Premium Pizza or type "next": ')
        if selected.lower() == 'next':
            break
        try:
            selected = int(selected) - 1
            if selected < 0 or selected >= len(premium_pizzas):
                print('Invalid Input')
            else:
                pizza_dict['num_premium_pizzas'] += 1
                num_pizzas -= 1
        except ValueError:
            print('Invalid Input')

    while num_pizzas > 0:
        selected = input('Select Your Gourmet Pizza or type "next": ')
        if selected.lower() == 'next':
            break
        try:
            selected = int(selected) - 1
            if selected < 0 or selected >= len(gourmet_pizzas):
                print('Invalid Input')
            else:
                pizza_dict['num_gourmet_pizzas'] += 1
                num_pizzas -= 1
        except ValueError:
            print('Invalid Input')

    return pizza_dict

def main():
    name = customer_name()
    phone = get_phone_number()
    address = delivery_details()
    pizza_order = pizza_list()

    print(f"\nOrder Summary:\nName: {name}\nPhone: {phone}\nAddress: {address}")
    print(f"Total number of premium pizzas: {pizza_order['num_premium_pizzas']}")
    print(f"Total number of gourmet pizzas: {pizza_order['num_gourmet_pizzas']}")

main()

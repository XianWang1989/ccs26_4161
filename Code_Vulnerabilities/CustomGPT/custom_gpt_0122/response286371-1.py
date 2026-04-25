
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme",
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]

gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"
]

phone_number = ""
delivery_address = ""
num_pizzas = -1

def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ")
        if not name.isalpha():
            print("Error: Name cannot be a number!")
            name = ""
    return name

def delivery_details():
    global delivery_address  # Declare the variable as global to modify it
    while delivery_address == "":
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address == "":
            print("Error: Address cannot be empty!")

def get_phone_number():
    global phone_number  # Declare the variable as global to modify it
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if phone_number < 1000000:  # Check for valid phone number length
                print("Phone number must be at least 7 digits.")
                continue
            break
        except ValueError:
            print("Phone number must be an integer only (no letters).")

def pizza_list():
    global num_pizzas  # Declare the variable as global to modify it
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input.')

    pizza_dict = {
        "premium_pizza_price": 8.50,
        "gourmet_pizza_price": 5.00,
        "num_premium_pizzas": 0,
        "num_gourmet_pizzas": 0
    }

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\nEnter "next" to move on.\n')

    for pizza_type in ['premium', 'gourmet']:
        remaining = num_pizzas
        while remaining > 0:
            selected = input(f'Select Your {pizza_type.capitalize()} Pizza (or type "next"): ')
            if selected == 'next':
                break
            try:
                selected = int(selected)
                if 1 <= selected <= (len(premium_pizzas) if pizza_type == 'premium' else len(gourmet_pizzas)):
                    if pizza_type == 'premium':
                        pizza_dict['num_premium_pizzas'] += 1
                    else:
                        pizza_dict['num_gourmet_pizzas'] += 1
                    remaining -= 1
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

    return pizza_dict

def main():
    customer = customer_name()
    get_phone_number()
    delivery_details()
    pizza_dict = pizza_list()

    # Print receipt
    print("\n=== Receipt ===")
    print(f"Customer Name: {customer}")
    print(f"Phone Number: {phone_number}")
    print(f"Delivery Address: {delivery_address}")
    print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")

main()


premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
    "Teeto shroomo supreme", "The volcanic rengar", 
    "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", 
    "Intergalactic BBQ", "BBQ Chicken", "Hellfire"
]

pizza_dict = {
    "premium_pizza_price": 8.50, 
    "gourmet_pizza_price": 5.00, 
    "selected_pizzas": 0, 
    "num_premium_pizzas": 0, 
    "num_gourmet_pizzas": 0
}

def main():
    customer_name()

def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ")
        if not name.isalpha():
            print("Error: Name must contain only letters.")
            name = ""  # Reset if not valid
    phone_number()

def phone_number():
    phone_number = -1
    while phone_number < 0 or len(str(phone_number)) < 7:
        try:
            phone_number = int(input("Please enter your phone number (at least 7 digits): "))
            if len(str(phone_number)) < 7:
                raise ValueError  # Trigger except block
        except ValueError:
            print("Phone number must be an integer with at least 7 digits.")
    delivery_details()

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        delivery_address = input("Please enter your delivery address: ")
    pizza_list()

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, 1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, 1):
        print(f"{i}. {pizza}")

    select_pizzas(num_pizzas)

def select_pizzas(num_pizzas):
    while num_pizzas > 0:
        selected = input('Select Your Premium Pizza (type "next" to finish): ')
        if selected == 'next':
            break
        try:
            selected = int(selected)
            if 1 <= selected <= len(premium_pizzas):
                pizza_dict['num_premium_pizzas'] += 1
                num_pizzas -= 1
            else:
                print('Invalid Input')
        except ValueError:
            print('Invalid Input')

    # Continue for gourmet pizzas
    while num_pizzas > 0:
        selected = input('Select Your Gourmet Pizza (type "next" to finish): ')
        if selected == 'next':
            break
        try:
            selected = int(selected)
            if 1 <= selected <= len(gourmet_pizzas):
                pizza_dict['num_gourmet_pizzas'] += 1
                num_pizzas -= 1
            else:
                print('Invalid Input')
        except ValueError:
            print('Invalid Input')

    print_receipt()

def print_receipt():
    print('\nReceipt:')
    print('Total number of premium pizzas:', pizza_dict['num_premium_pizzas'])
    print('Total number of gourmet pizzas:', pizza_dict['num_gourmet_pizzas'])

main()

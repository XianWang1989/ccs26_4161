
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
                  "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", 
                  "Vegetriano"]

gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
                  "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50, 
    "gourmet_pizza_price": 5.00, 
    "selected_pizzas": 0, 
    "num_premium_pizzas": 0, 
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if not name.isalpha():
                raise ValueError("Name cannot be a number or empty!")
            return name
        except ValueError as ve:
            print(ve)

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if not address:
                raise ValueError("Delivery address cannot be empty!")
            return address
        except ValueError as ve:
            print(ve)

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number (numeric only): "))
            if phone_number < 1000000:  # Basic check for a phone number length (e.g., 7 digits)
                raise ValueError("Phone number must be at least 7 digits!")
            return phone_number
        except ValueError as ve:
            print(ve)

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    # Select Premium Pizzas
    select_pizzas(num_pizzas, premium_pizzas, "premium")
    # Select Gourmet Pizzas
    select_pizzas(num_pizzas, gourmet_pizzas, "gourmet")

def select_pizzas(num_pizzas, pizza_list, pizza_type):
    for _ in range(num_pizzas):
        while True:
            try:
                selected = input(f'Select Your {pizza_type.capitalize()} Pizza: ')
                if selected.lower() == 'next':
                    break
                selected = int(selected)
                if selected <= 0 or selected > len(pizza_list):
                    print('Invalid Input')
                else:
                    pizza_dict[f'num_{pizza_type}_pizzas'] += 1
                    break
            except ValueError:
                print('Invalid Input')

def main():
    customer = customer_name()
    phone = get_phone_number()
    address = delivery_details()
    pizza_list()

    # Store all relevant information in a list
    receipt = [customer, phone, address, pizza_dict['num_premium_pizzas'], pizza_dict['num_gourmet_pizzas']]
    print("Receipt Information:")
    print(f"Customer Name: {receipt[0]}")
    print(f"Phone Number: {receipt[1]}")
    print(f"Delivery Address: {receipt[2]}")
    print(f"Number of premium pizzas: {receipt[3]}")
    print(f"Number of gourmet pizzas: {receipt[4]}")

    total_cost = (receipt[3] * pizza_dict['premium_pizza_price'] + 
                  receipt[4] * pizza_dict['gourmet_pizza_price'])
    print(f'Total cost: {total_cost}')

main()

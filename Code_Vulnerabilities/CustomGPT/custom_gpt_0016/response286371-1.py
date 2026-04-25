
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

def input_customer_name():
    customer_name = ""
    while not customer_name:
        customer_name = input("Please enter your name: ")
        if customer_name.isdigit():
            print("Error: Name cannot be a number!")
            customer_name = ""
    return customer_name

def input_phone_number():
    phone_number = -1
    while phone_number < 0 or len(str(phone_number)) < 7:
        try:
            phone_number = int(input("Please enter your phone number (minimum 7 digits): "))
        except ValueError:
            print("Error: Phone number must be an integer only.")
    return phone_number

def input_delivery_details():
    delivery_address = ""
    while not delivery_address:
        delivery_address = input("Please enter your delivery address: ")
    return delivery_address

def input_pizza_quantity():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input, please enter a number.')
    return num_pizzas

def select_pizzas(num_pizzas):
    for i in range(num_pizzas):
        print('\n== Premium Pizzas ==\n')
        for idx, pizza in enumerate(premium_pizzas, start=1):
            print(f'{idx}. {pizza}')

        while True:
            selected = input('Select your premium pizza by number (or type "next" to skip): ')
            if selected.lower() == 'next':
                break
            try:
                selected = int(selected)
                if 1 <= selected <= len(premium_pizzas):
                    pizza_dict['num_premium_pizzas'] += 1
                    break
                else:
                    print('Invalid selection, try again.')
            except ValueError:
                print('Invalid input, please enter a number.')

def main():
    customer_name = input_customer_name()
    phone_number = input_phone_number()
    delivery_address = input_delivery_details()

    num_pizzas = input_pizza_quantity()
    select_pizzas(num_pizzas)

    print(f'\nOrder Summary for {customer_name}:')
    print(f'Phone Number: {phone_number}')
    print(f'Delivery Address: {delivery_address}')
    print(f'Number of Premium Pizzas: {pizza_dict["num_premium_pizzas"]}')

if __name__ == "__main__":
    main()

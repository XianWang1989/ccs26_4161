
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def get_customer_name():
    while True:
        customer_name = input("Please enter your name: ")
        if customer_name.isalpha():
            return customer_name
        print("Error: Name must not be a number.")

def get_delivery_details():
    while True:
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address:
            return delivery_address
        print("Error: You must enter something!")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number: "))
            if len(str(phone_number)) >= 7:
                return phone_number
            else:
                print("Phone number must have at least 7 digits.")
        except ValueError:
            print("Phone number must be an integer.")

def get_num_pizzas():
    while True:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if 0 < num_pizzas <= 5:
                return num_pizzas
            else:
                print('Invalid Input: Must be between 1 and 5.')
        except ValueError:
            print('Invalid Input: Please enter a number.')

def pizza_list(num_pizzas):
    print('\n== Premium Pizzas ==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n== Gourmet Pizzas ==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    # Input for premium pizzas
    for _ in range(num_pizzas):
        while True:
            selected = input('Select Your Premium Pizza or enter "next": ')
            if selected == 'next':
                break
            try:
                selected = int(selected)
                if 1 <= selected <= len(premium_pizzas):
                    pizza_dict['num_premium_pizzas'] += 1
                    break
                else:
                    print('Invalid Input. Select a valid pizza number.')
            except ValueError:
                print('Invalid Input. Enter a number.')

    # Input for gourmet pizzas
    for _ in range(num_pizzas):
        while True:
            selected = input('Select Your Gourmet Pizza or enter "next": ')
            if selected == 'next':
                break
            try:
                selected = int(selected)
                if 1 <= selected <= len(gourmet_pizzas):
                    pizza_dict['num_gourmet_pizzas'] += 1
                    break
                else:
                    print('Invalid Input. Select a valid pizza number.')
            except ValueError:
                print('Invalid Input. Enter a number.')

def main():
    customer_name = get_customer_name()
    delivery_address = get_delivery_details()
    phone_number = get_phone_number()
    num_pizzas = get_num_pizzas()
    pizza_list(num_pizzas)

    # Print the receipt
    print(f"\nReceipt for {customer_name}:")
    print(f"Delivery Address: {delivery_address}")
    print(f"Phone Number: {phone_number}")
    print('Total number of premium pizzas: ' + str(pizza_dict['num_premium_pizzas']))
    print('Total number of gourmet pizzas: ' + str(pizza_dict['num_gourmet_pizzas']))
    cost = (pizza_dict["num_premium_pizzas"] * pizza_dict['premium_pizza_price']) + (pizza_dict["num_gourmet_pizzas"] * pizza_dict['gourmet_pizza_price'])
    print('Total cost: ' + str(cost))

main()

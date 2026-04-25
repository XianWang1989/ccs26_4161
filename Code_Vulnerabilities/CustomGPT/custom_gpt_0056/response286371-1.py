
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme",
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name and not name.isdigit():
            return name
        else:
            print("Error: You must enter a valid name (cannot be a number).")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        else:
            print("Error: You must enter a delivery address.")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number: "))
            if len(str(phone_number)) >= 7:  # Check if at least 7 digits
                return phone_number
            else:
                print("Error: Phone number must be at least 7 digits long.")
        except ValueError:
            print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (1-5): '))
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 5.')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, 1):
        print(f"{i}. {pizza}")
    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, 1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):
        while True:
            selected = input('Select Your Premium Pizza (or type "next" to proceed): ')
            if selected.lower() == 'next':
                break
            try:
                selected = int(selected)
                if 1 <= selected <= len(premium_pizzas):
                    pizza_dict['num_premium_pizzas'] += 1
                    break
                else:
                    print('Invalid input. Choose a valid number.')
            except ValueError:
                print('Invalid input. Please enter a number.')

        while True:
            selected = input('Select Your Gourmet Pizza (or type "next" to proceed): ')
            if selected.lower() == 'next':
                break
            try:
                selected = int(selected)
                if 1 <= selected <= len(gourmet_pizzas):
                    pizza_dict['num_gourmet_pizzas'] += 1
                    break
                else:
                    print('Invalid input. Choose a valid number.')
            except ValueError:
                print('Invalid input. Please enter a number.')

def main():
    name = customer_name()
    phone_number = get_phone_number()
    delivery_info = delivery_details()

    pizza_list()  # Call pizza_list function here

    print("\nReceipt Summary:")
    print(f"Customer Name: {name}")
    print(f"Phone Number: {phone_number}")
    print(f"Delivery Address: {delivery_info}")
    print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")
    cost = (pizza_dict["num_premium_pizzas"] * pizza_dict['premium_pizza_price']) + \
           (pizza_dict["num_gourmet_pizzas"] * pizza_dict['gourmet_pizza_price'])
    print(f'Total cost: ${cost:.2f}')

main()

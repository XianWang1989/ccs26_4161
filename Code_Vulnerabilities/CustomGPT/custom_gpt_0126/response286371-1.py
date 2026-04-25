
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        customer_name = input("Please enter your name: ")
        if customer_name.isalpha():  # Ensure it's not a number
            return customer_name
        else:
            print("Error: Name cannot be a number. Please enter a valid name.")

def delivery_details():
    while True:
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address:
            return delivery_address
        else:
            print("Error: Address cannot be empty.")

def phone_number_input():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if len(str(phone_number)) >= 7:
                return phone_number
            else:
                print("Error: Phone number must be at least 7 digits.")
        except ValueError:
            print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input.')

    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i + len(premium_pizzas)}. {pizza}")

    select_pizzas(num_pizzas)

def select_pizzas(num_pizzas):
    while num_pizzas > 0:
        selected = input('Select Your Pizza (enter number or "next" to proceed): ')
        if selected.lower() == 'next':
            break
        try:
            selected = int(selected)
            if selected <= len(premium_pizzas):
                pizza_dict['num_premium_pizzas'] += 1
                num_pizzas -= 1
            elif selected <= len(premium_pizzas) + len(gourmet_pizzas):
                pizza_dict['num_gourmet_pizzas'] += 1
                num_pizzas -= 1
            else:
                print('Invalid Input.')
        except ValueError:
            print('Invalid Input.')

# Initial function calls to gather user data
customer = customer_name()
phone = phone_number_input()
address = delivery_details()
pizza_list()

# Print receipt information
print(f"\nCustomer Name: {customer}")
print(f"Phone Number: {phone}")
print(f"Delivery Address: {address}")
print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")
cost = (pizza_dict["num_premium_pizzas"] * pizza_dict['premium_pizza_price']) + (pizza_dict["num_gourmet_pizzas"] * pizza_dict['gourmet_pizza_price'])
print(f'Total cost: {cost:.2f}')

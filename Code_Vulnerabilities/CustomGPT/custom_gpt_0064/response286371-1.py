
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
        try:
            name = input("Please enter your name: ")
            if name.isalpha() and name:
                return name
            else:
                print("Error: Name cannot be empty or numerical.")
        except Exception as e:
            print(f"Error: {e}")

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address:
                return address
            else:
                print("Error: Address cannot be empty.")
        except Exception as e:
            print(f"Error: {e}")

def phone_number():
    while True:
        try:
            number = input("Please enter your phone number: ")
            if number.isdigit() and len(number) >= 7:
                return number
            else:
                print("Error: Phone number must be at least 7 digits.")
        except Exception as e:
            print(f"Error: {e}")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input')

    # Show pizza options
    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas):
        print(f"{i + 1}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas):
        print(f"{i + 1}. {pizza}")

    selected_pizzas = []
    while num_pizzas > 0:
        selected = input('Select your pizza (or type "next" to finish): ')
        if selected == 'next':
            break
        try:
            selected = int(selected) - 1
            if selected < 0 or selected >= len(premium_pizzas) + len(gourmet_pizzas):
                print('Invalid selection')
            else:
                selected_pizzas.append(selected)
                num_pizzas -= 1
        except ValueError:
            print('Invalid input')

    return selected_pizzas

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery or 2 for pickup: ")
        if get_user_info == "1":
            return "delivery"
        elif get_user_info == "2":
            return "pickup"
        else:
            print("Invalid input.")

# Main program execution
name = customer_name()
address = ''
phone = phone_number()
food_mode = user_info()

if food_mode == "delivery":
    address = delivery_details()

selected_pizzas = pizza_list()

# Print receipt
print(f"\nName: {name}")
print(f"Phone: {phone}")
if address:
    print(f"Delivery Address: {address}")
print(f"Selected Pizzas: {selected_pizzas}")

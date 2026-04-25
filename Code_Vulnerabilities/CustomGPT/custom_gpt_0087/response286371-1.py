
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        name = input("Please enter your name: ").strip()
        if name:
            return name
        else:
            print("Error! You must enter your name.")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ").strip()
        if address:
            return address
        else:
            print("Error! You must enter something.")

def phone_number():
    while True:
        try:
            number = int(input("Please enter your phone number:\n\t"))
            if len(str(number)) >= 7:  # Check if it's a valid number.
                return number
            else:
                print("Phone number must be at least 7 digits.")
        except ValueError:
            print("Phone number must be an integer only (no letters).")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if not (1 <= num_pizzas <= 5):
                print('Invalid input, please enter a number between 1 and 5.')
        except ValueError:
            print('Invalid input, please enter an integer.')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f'{i}. {pizza}')

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f'{i}. {pizza}')

    selected_pizzas = []  # Store selected pizzas
    for _ in range(num_pizzas):
        selected = input('Select Your Premium Pizza by number: ')
        if selected.isdigit() and 1 <= int(selected) <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1
            selected_pizzas.append(premium_pizzas[int(selected) - 1])  # Store selected pizza
        else:
            print('Invalid Input for Premium Pizza.')

    return selected_pizzas

def user_info():
    while True:
        choice = input("Press 1 for delivery, press 2 for pickup: ")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            pizza_list()
            break
        else:
            print("Invalid choice, please select 1 or 2.")

def main():
    name = customer_name()
    number = phone_number()
    user_info()
    print(f"\nCustomer: {name}, Phone: {number}")
    print(f"Order Summary: {pizza_dict['num_premium_pizzas']} premium pizzas ordered.")

main()

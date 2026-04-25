
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham" , "Vegetriano" ]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50, 
    "gourmet_pizza_price": 5.00, 
    "selected_pizzas": 0, 
    "num_premium_pizzas": 0, 
    "num_gourmet_pizzas": 0
}

def get_non_empty_input(prompt):
    user_input = ""
    while user_input.strip() == "":
        user_input = input(prompt)
    return user_input.strip()

def customer_name():
    name = get_non_empty_input("Please enter your name: ")
    return name

def delivery_details():
    delivery_address = get_non_empty_input("Please enter your delivery address: ")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if len(str(phone_number)) < 7:
                print("Phone number must be at least 7 digits.")
                continue
            return phone_number
        except ValueError:
            print("Phone number must be integer only (no letters or symbols).")

def pizza_list():
    num_pizzas = -1
    while (num_pizzas < 1) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input('Select Your Premium Pizza (or enter 0 to skip): '))
                if selected == 0:
                    break
                if selected < 1 or selected > len(premium_pizzas):
                    print('Invalid Input')
                else:
                    pizza_dict['num_premium_pizzas'] += 1
                    pizza_dict['selected_pizzas'] += 1
                    break
            except ValueError:
                print('Invalid Input')

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input('Select Your Gourmet Pizza (or enter 0 to skip): '))
                if selected == 0:
                    break
                if selected < 1 or selected > len(gourmet_pizzas):
                    print('Invalid Input')
                else:
                    pizza_dict['num_gourmet_pizzas'] += 1
                    pizza_dict['selected_pizzas'] += 1
                    break
            except ValueError:
                print('Invalid Input')

def user_info():
    while True:
        choice = input("Press 1 for delivery\nPress 2 for pickup\n\t:")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            pizza_list()
            break
        else:
            print("Invalid choice, please try again.")

# Start of the program
name = customer_name()
phone_number = get_phone_number()
user_info()

# Print details at the end
print(f"\nCustomer Name: {name}")
print(f"Phone Number: {phone_number}")
print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")
cost = (pizza_dict["num_premium_pizzas"] * pizza_dict['premium_pizza_price']) + (pizza_dict["num_gourmet_pizzas"] * pizza_dict['gourmet_pizza_price'])
print(f'Total cost: {cost}')

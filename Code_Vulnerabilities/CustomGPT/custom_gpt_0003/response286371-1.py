
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "selected_pizzas": 0, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

def customer_name():
    name = ""
    while name == "":
        try:
            name = input("Please enter your name: ")
            if name.isdigit():
                raise ValueError("Name cannot be a number!")
        except ValueError as e:
            print(f"Error: {e}")
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = input("Please enter your delivery address: ")
        except Exception:
            print("Error: Delivery address cannot be empty!")

def get_phone_number():
    phone_number = ""
    while len(phone_number) < 7 or not phone_number.isdigit():
        try:
            phone_number = input("Please enter your phone number (at least 7 digits):\n")
            if len(phone_number) < 7 or not phone_number.isdigit():
                raise ValueError("Phone number must be at least 7 digits and numeric.")
        except ValueError as e:
            print(f"Error: {e}")
    return phone_number

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 5.')

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")
    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    for pizza_type in ['premium', 'gourmet']:
        while num_pizzas > 0:
            selected = input(f'Select Your {pizza_type.capitalize()} Pizza (or type "next" to continue): ')
            if selected == 'next':
                break
            try:
                selected = int(selected)
                if selected < 1 or (pizza_type == 'premium' and selected > len(premium_pizzas)) or (pizza_type == 'gourmet' and selected > len(gourmet_pizzas)):
                    print('Invalid Input')
                else:
                    pizza_dict[f'num_{pizza_type}_pizzas'] += 1
                    num_pizzas -= 1
            except ValueError:
                print('Invalid Input')

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery, Press 2 for pickup:\n")
        if get_user_info == "1":
            delivery_details()
            break
        elif get_user_info == "2":
            break

# Main Program Execution
name = customer_name()
phone_number = get_phone_number()
user_info()
pizza_list()

# Optional: Printing the receipt or summary
print(f"\nThank you for your order, {name}! We'll call you at {phone_number} for delivery!")
print(f'Total number of premium pizzas: {pizza_dict["num_premium_pizzas"]}')
print(f'Total number of gourmet pizzas: {pizza_dict["num_gourmet_pizzas"]}')

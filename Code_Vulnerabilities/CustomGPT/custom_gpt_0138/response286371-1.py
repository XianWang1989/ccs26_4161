
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "selected_pizzas": 0,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0,
}

def customer_name():
    name = ""
    while name == "":
        try:
            name = str(input("Please enter your name: "))
        except:
            print("Error: you must enter something (cannot be a number).")
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = str(input("Please enter your delivery address: "))
        except:
            print("Error: you must enter something.")

def phone_number():
    number = 0
    while (number < 0) or (number < 1000000):  # A simple check for valid phone number
        try:
            number = int(input("Please enter your phone number:\n\t"))
        except:
            print("Phone number must be an integer only (no letters).")
    return number

def pizza_list():
    num_pizzas = -1
    while (num_pizzas <= 0) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except:
            print('Invalid Input, please enter a number.')

    show_pizza_menu(num_pizzas)

def show_pizza_menu(num_pizzas):
    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")
    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    # Select pizzas
    select_pizzas(num_pizzas)

def select_pizzas(num_pizzas):
    while num_pizzas > 0:
        selected = input('Select Your Premium Pizza (or type "next" to continue): ')
        if selected == 'next':
            break
        try:
            selected = int(selected)
            if 1 <= selected <= len(premium_pizzas):
                pizza_dict['num_premium_pizzas'] += 1
                num_pizzas -= 1
            else:
                print('Invalid Input')
        except:
            print('Invalid Input, please enter a number.')

    # Repeat for gourmet pizzas (similar logic here)

def user_info():
    while True:
        get_user_info = str(input("Press 1 for delivery, Press 2 for pickup: "))
        if get_user_info == "1":
            delivery_details()
            break
        elif get_user_info == "2":
            pizza_list()
            break

# Run the program
name = customer_name()
phone = phone_number()
user_info()

# Display receipt
print(f"\nCustomer Name: {name}")
print(f"Phone Number: {phone}")
print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
# Include additional receipt details as needed.


premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.isdigit():
                raise ValueError("Name cannot be a number!")
            return name
        except ValueError as e:
            print(f"Error: {e}")

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address == "":
                raise ValueError("Address cannot be empty!")
            return address
        except ValueError as e:
            print(f"Error: {e}")

def phone_number():
    while True:
        try:
            number = input("Please enter your phone number:\n\t")
            if not number.isdigit() or len(number) < 7:
                raise ValueError("Phone number must be at least 7 digits long!")
            return number
        except ValueError as e:
            print(f"Error: {e}")

def pizza_list():
    num_pizzas = -1
    while (num_pizzas <= 0) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    pizza_dict = {
        "premium_pizza_price": 8.50,
        "gourmet_pizza_price": 5.00,
        "num_premium_pizzas": 0,
        "num_gourmet_pizzas": 0
    }

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    while True:
        if num_pizzas == 0:
            break
        selected = input('Select Your Pizza or "next" to finish: ')
        if selected == 'next':
            break
        else:
            try:
                selected = int(selected)
                if selected <= 0 or (selected > len(premium_pizzas) and selected > len(gourmet_pizzas)):
                    print('Invalid Input')
                else:
                    if selected <= len(premium_pizzas):
                        pizza_dict['num_premium_pizzas'] += 1
                    else:
                        pizza_dict['num_gourmet_pizzas'] += 1
                    num_pizzas -= 1
            except ValueError:
                print('Invalid Input')

    return pizza_dict

def user_info():
    get_user_info = ""
    while get_user_info not in ["1", "2"]:
        get_user_info = input("Press 1 for delivery or Press 2 for pickup: ")

    if get_user_info == "1":
        delivery_details()

    elif get_user_info == "2":
        pizza_list()

# Main Execution
user_details = {
    "name": customer_name(),
    "phone": phone_number()
}
user_info()

# After the order, you can access user details
print("User details:", user_details)

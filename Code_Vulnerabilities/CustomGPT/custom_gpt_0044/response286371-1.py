
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    name = ""
    while name == "":
        try:
            name = input("Please enter your name: ")
            if name.isdigit():
                raise ValueError("Name cannot be a number")
        except ValueError as e:
            print(f"Error: {e}")
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = input("Please enter your delivery address: ")
        except Exception:
            print("Error: you must enter something!")
    return delivery_address

def phone_number():
    phone = -1
    while phone < 0 or len(str(phone)) < 7:
        try:
            phone = int(input("Please enter your phone number:\n\t"))
            if len(str(phone)) < 7:
                raise ValueError("Phone number must have at least 7 digits.")
        except ValueError as e:
            print(f"Error: {e}")
    return phone

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
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
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    for category in ["premium", "gourmet"]:
        while num_pizzas > 0:
            selected = input(f'Select Your {category.capitalize()} Pizza (or type "next" to continue): ')
            if selected.lower() == 'next':
                break
            try:
                selected = int(selected)
                if selected <= 0 or selected > len(premium_pizzas if category == "premium" else gourmet_pizzas):
                    print('Invalid Input')
                else:
                    pizza_dict[f'num_{category}_pizzas'] += 1
                    num_pizzas -= 1
            except ValueError:
                print('Invalid Input')

    return pizza_dict

def user_info():
    while True:
        option = input("Press 1 for delivery or 2 for pickup: ")
        if option == "1":
            delivery_details()
            break
        elif option == "2":
            pizza_list()
            break

# Main program flow
name = customer_name()
phone = phone_number()
user_info()

# Print the collected info
print(f"\nCustomer Name: {name}\nPhone Number: {phone}")

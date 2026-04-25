
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
        try:
            name = input("Please enter your name: ")
            if name.strip() == "":
                raise ValueError("Name cannot be empty")
            return name
        except ValueError as e:
            print(e)

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address.strip() == "":
                raise ValueError("Address cannot be empty")
            return address
        except ValueError as e:
            print(e)

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number:\n\t"))
            if phone < 1000000 or phone > 9999999:  # Ensure 7 digits
                raise ValueError("Phone number must be a 7-digit number")
            return phone
        except ValueError as e:
            print(e)

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input')
    return num_pizzas

def select_pizza(num_pizzas):
    for category, pizzas in [('Premium', premium_pizzas), ('Gourmet', gourmet_pizzas)]:
        print(f'\n=={category} Pizzas==\n')
        for i, pizza in enumerate(pizzas, start=1):
            print(f'{i}. {pizza}')

        for _ in range(num_pizzas):
            while True:
                try:
                    selected = int(input(f'Select Your {category} Pizza (1-{len(pizzas)}) or enter 0 to skip: '))
                    if selected < 0 or selected > len(pizzas):
                        print('Invalid input')
                    elif selected > 0:
                        if category == 'Premium':
                            pizza_dict['num_premium_pizzas'] += 1
                        else:
                            pizza_dict['num_gourmet_pizzas'] += 1
                        break
                    else:
                        break
                except ValueError:
                    print('Invalid input')

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery, Press 2 for pickup: ")
        if get_user_info == "1":
            delivery_details()
            break
        elif get_user_info == "2":
            return

# Main program execution
name = customer_name()
phone = phone_number()
num_pizzas = pizza_list()
select_pizza(num_pizzas)

# Display the total number of pizzas ordered
print(f"\nTotal number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")

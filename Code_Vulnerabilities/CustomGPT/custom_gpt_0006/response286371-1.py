
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", 
    "Intergalactic BBQ", "BBQ Chicken", "Hellfire"
]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def get_customer_name():
    while True:
        customer_name = input("Please enter your name: ").strip()
        if customer_name:
            return customer_name
        else:
            print("Error: You must enter a name!")

def get_delivery_details():
    delivery_address = ""
    while not delivery_address:
        delivery_address = input("Please enter your delivery address: ").strip()
        if not delivery_address:
            print("Error: You must enter an address!")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n"))
            if len(str(phone_number)) >= 7:  # Check if phone number is valid
                return phone_number
            else:
                print("Phone number must be at least 7 digits!")
        except ValueError:
            print("Phone number must be an integer only.")

def get_num_pizzas():
    while True:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if 0 < num_pizzas <= 5:
                return num_pizzas
            else:
                print('Invalid Input. Must be between 1 and 5.')
        except ValueError:
            print('Invalid Input. Must be a number.')

def select_pizzas(num_pizzas, pizza_type):
    while num_pizzas > 0:
        print(f'\n=={pizza_type} Pizzas==\n')
        pizzas = premium_pizzas if pizza_type == "Premium" else gourmet_pizzas
        for i, pizza in enumerate(pizzas):
            print(f"{i + 1}. {pizza}")

        selected = input(f'Select Your {pizza_type} Pizza (or "next" to continue): ')
        if selected.lower() == 'next':
            break
        else:
            try:
                selected = int(selected)
                if 1 <= selected <= len(pizzas):
                    if pizza_type == "Premium":
                        pizza_dict['num_premium_pizzas'] += 1
                    else:
                        pizza_dict['num_gourmet_pizzas'] += 1
                    num_pizzas -= 1
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery, Press 2 for pickup: ")
        if get_user_info == "1":
            get_delivery_details()
            break
        elif get_user_info == "2":
            break

# Main function flow
customer_name = get_customer_name()
phone_number = get_phone_number()
num_pizzas = get_num_pizzas()

select_pizzas(num_pizzas, "Premium")
select_pizzas(num_pizzas, "Gourmet")
user_info()

# Receipt output
print(f'\nTotal number of premium pizzas: {pizza_dict["num_premium_pizzas"]}')
print(f'Total number of gourmet pizzas: {pizza_dict["num_gourmet_pizzas"]}')

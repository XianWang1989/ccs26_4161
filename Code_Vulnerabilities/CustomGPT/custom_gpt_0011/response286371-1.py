
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham" , "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

user_info = {
    'customer_name': '',
    'delivery_address': '',
    'phone_number': 0,
    'num_premium_pizzas': 0,
    'num_gourmet_pizzas': 0
}

def get_customer_name():
    while user_info['customer_name'] == "":
        user_info['customer_name'] = input("Please enter your name: ")
        if not user_info['customer_name'].isalpha():
            print("Error: Name must not contain numbers. Please try again.")
            user_info['customer_name'] = ''

def get_delivery_details():
    while user_info['delivery_address'] == "":
        user_info['delivery_address'] = input("Please enter your delivery address: ")

def get_phone_number():
    while user_info['phone_number'] <= 0 or len(str(user_info['phone_number'])) < 7:
        try:
            user_info['phone_number'] = int(input("Please enter your phone number:\n\t"))
        except ValueError:
            print("Error: Phone number must be an integer.")

def get_pizza_quantity():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input. Please enter a number between 1 and 5.')
    return num_pizzas

def select_pizzas(num_pizzas, pizza_type):
    print(f'\n=={pizza_type} Pizzas==\n')
    pizzas = premium_pizzas if pizza_type == "Premium" else gourmet_pizzas
    for i, pizza in enumerate(pizzas):
        print(f"{i + 1}. {pizza}")

    for _ in range(num_pizzas):
        selected = 0
        while selected <= 0 or selected > len(pizzas):
            try:
                selected = int(input(f'Select Your {pizza_type} Pizza (1-{len(pizzas)}): '))
            except ValueError:
                print('Invalid Input')
                selected = 0
        if pizza_type == "Premium":
            user_info['num_premium_pizzas'] += 1
        else:
            user_info['num_gourmet_pizzas'] += 1

def main():
    get_customer_name()
    get_delivery_details()
    get_phone_number()
    num_premium_pizzas = get_pizza_quantity()
    select_pizzas(num_premium_pizzas, "Premium")
    num_gourmet_pizzas = get_pizza_quantity()
    select_pizzas(num_gourmet_pizzas, "Gourmet")

    print("\nUser Info:")
    for key, value in user_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()

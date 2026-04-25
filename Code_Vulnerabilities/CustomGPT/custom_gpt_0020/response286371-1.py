
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
                  "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ")
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        delivery_address = input("Please enter your delivery address: ")
    return delivery_address

def get_phone_number():
    phone_number = -1
    while phone_number < 0 or len(str(phone_number)) < 7:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
        except ValueError:
            print("Phone number must be integer only.")
    return phone_number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like to order (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, 1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, 1):
        print(f"{i}. {pizza}")

    selected_pizzas = []

    for pizza_type, count in [('Premium', pizza_dict['num_premium_pizzas']), ('Gourmet', pizza_dict['num_gourmet_pizzas'])]:
        for _ in range(num_pizzas):
            try:
                selected = input(f'Select Your {pizza_type} Pizza (or type "next" to continue): ')
                if selected.lower() == 'next':
                    break
                else:
                    selected = int(selected)
                    if selected <= 0 or selected > (len(premium_pizzas) if pizza_type == 'Premium' else len(gourmet_pizzas)):
                        print('Invalid Input')
                    else:
                        if pizza_type == 'Premium':
                            pizza_dict['num_premium_pizzas'] += 1
                        else:
                            pizza_dict['num_gourmet_pizzas'] += 1
                        selected_pizzas.append(selected)
            except ValueError:
                print('Invalid Input')

    return selected_pizzas

def user_info():
    print("Press 1 for delivery or 2 for pickup:")
    choice = input()
    if choice == "1":
        delivery_details()
    elif choice == "2":
        pizza_list()

def main():
    name = customer_name()
    phone_number = get_phone_number()
    selected_pizzas = pizza_list()

    print(f"Customer Name: {name}")
    print(f"Phone Number: {phone_number}")
    # You can print selected pizzas information if needed

main()

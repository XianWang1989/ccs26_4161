
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

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
    address = ""
    while address == "":
        address = input("Please enter your delivery address: ")
    return address

def phone_number_input():
    phone_number = ""
    while len(phone_number) < 7 or not phone_number.isdigit():
        phone_number = input("Please enter your phone number (at least 7 digits): ")
    return phone_number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for category in ['premium', 'gourmet']:
        while num_pizzas > 0:
            if category == 'premium':
                print('\n==Premium Pizzas==\n')
                for i, pizza in enumerate(premium_pizzas):
                    print(f"{i + 1}. {pizza}")

            if category == 'gourmet':
                print('\n==Gourmet Pizzas==\n')
                for i, pizza in enumerate(gourmet_pizzas):
                    print(f"{i + 1}. {pizza}")

            selected = input(f'Select Your {category.capitalize()} Pizza (or type "next" to move on): ')
            if selected == 'next':
                break
            else:
                try:
                    selected = int(selected)
                    if selected <= 0 or (category == 'premium' and selected > len(premium_pizzas)) or (category == 'gourmet' and selected > len(gourmet_pizzas)):
                        print('Invalid Input')
                    else:
                        if category == 'premium':
                            pizza_dict['num_premium_pizzas'] += 1
                        else:
                            pizza_dict['num_gourmet_pizzas'] += 1
                        num_pizzas -= 1
                except ValueError:
                    print('Invalid Input')        

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery, Press 2 for pickup: ")
        if get_user_info == "1":
            delivery_details()
            break
        elif get_user_info == "2":
            pizza_list()
            break

# Main program
name = customer_name()
phone = phone_number_input()
user_info()

# Print summary (just an example)
print(f"Customer Name: {name}") 
print(f"Phone Number: {phone}") 
print(f"Total Premium Pizzas: {pizza_dict['num_premium_pizzas']}")
print(f"Total Gourmet Pizzas: {pizza_dict['num_gourmet_pizzas']}")

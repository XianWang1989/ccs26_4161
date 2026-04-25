
premium_pizzas = [
    "Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", 
    "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}
user_info_list = []

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name.isalpha():  # Check if the input is alphabetic
            user_info_list.append(name)
            break
        print("Error: You must enter a valid name!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:  # Check if the input is not empty
            user_info_list.append(address)
            break
        print("Error: You must enter a delivery address!")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number (digits only): "))
            if len(str(phone)) >= 7:  # Ensure a valid phone number
                user_info_list.append(phone)
                break
            else:
                print("Error: Phone number must be at least 7 digits!")
        except ValueError:
            print("Error: Phone number must be an integer!")

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input, please try again.')

    # Display pizza options
    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, 1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, 1):
        print(f"{i}. {pizza}")

    for category in ['premium', 'gourmet']:
        for _ in range(num_pizzas):
            while True:
                selected = input(f'Select Your {category.capitalize()} Pizza or type "next" to skip: ')
                if selected.lower() == 'next':
                    break
                try:
                    selected = int(selected)
                    if 1 <= selected <= len(premium_pizzas if category == 'premium' else gourmet_pizzas):
                        if category == 'premium':
                            pizza_dict['num_premium_pizzas'] += 1
                        else:
                            pizza_dict['num_gourmet_pizzas'] += 1
                        break
                    else:
                        print('Invalid Input')
                except ValueError:
                    print('Invalid Input')

def user_info():
    get_user_info = ""
    while get_user_info not in ["1", "2"]:
        get_user_info = input("Press 1 for delivery, Press 2 for pickup: ")
    if get_user_info == "1":
        delivery_details()
    elif get_user_info == "2":
        pizza_list()

# Running the program
customer_name()
phone_number()
user_info()
print('\nUser Info:', user_info_list)
print('Total number of premium pizzas:', pizza_dict['num_premium_pizzas'])
print('Total number of gourmet pizzas:', pizza_dict['num_gourmet_pizzas'])

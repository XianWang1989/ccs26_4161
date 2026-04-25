
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}
user_info_list = []

def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ")
    user_info_list.append(name)

def delivery_details():
    address = ""
    while address == "":
        address = input("Please enter your delivery address: ")
    user_info_list.append(address)

def phone_number_input():
    phone_number = -1
    while phone_number < 0 or phone_number < 7:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
        except ValueError:
            print("Phone number must be an integer only.")
    user_info_list.append(phone_number)

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    select_pizza(num_pizzas)

def select_pizza(num_pizzas):
    while num_pizzas > 0:
        selected = input('Select Your Premium Pizza (or type "next" to proceed): ')
        if selected.lower() == 'next':
            break
        try:
            selected = int(selected)
            if 1 <= selected <= len(premium_pizzas):
                pizza_dict['num_premium_pizzas'] += 1
                num_pizzas -= 1
            else:
                print('Invalid Input')
        except ValueError:
            print('Invalid Input')

def user_info():
    while True:
        choice = input("Press 1 for delivery, Press 2 for pickup: ")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            break

# Main execution flow
customer_name()
phone_number_input()
user_info()
pizza_list()

# Print user info
print("User Information:")
for info in user_info_list:
    print(info)

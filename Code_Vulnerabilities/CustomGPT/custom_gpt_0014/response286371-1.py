
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

user_info_list = []

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if not name.isdigit() and name.strip() != "":
                user_info_list.append(name)
                break
            else:
                print("Error: Name cannot be a number or empty.")
        except Exception:
            print("Error: Please enter a valid name.")

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address.strip() != "":
                user_info_list.append(address)
                break
            else:
                print("Error: Address cannot be empty.")
        except Exception:
            print("Error: Please enter a valid address.")

def phone_number_input():
    while True:
        try:
            phone_number = int(input("Please enter your phone number (digits only): "))
            if phone_number > 0 and len(str(phone_number)) == 10: # Assuming a 10-digit number
                user_info_list.append(phone_number)
                break
            else:
                print("Error: Please enter a valid 10-digit phone number.")
        except ValueError:
            print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if num_pizzas < 1 or num_pizzas > 5:
                print("Invalid Input: Must order 1 to 5 pizzas.")
        except ValueError:
            print('Invalid Input: Must be an integer.')

    pizza_dict = {"num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas):
        print(f"{i + 1}. {pizza}")
    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas):
        print(f"{i + 1}. {pizza}")

def main():
    customer_name()
    delivery_details()
    phone_number_input()
    pizza_list()

    print("\nUser Information:")
    for info in user_info_list:
        print(info)

main()

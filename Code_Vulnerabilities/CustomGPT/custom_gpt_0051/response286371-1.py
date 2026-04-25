
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
        name = input("Please enter your name: ").strip()
        if name:
            return name
        print("Error: You must enter a valid name!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ").strip()
        if address:
            return address
        print("Error: You must enter a valid address!")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number:\n\t"))
            if phone > 999999:  # Basic check for valid phone number
                return phone
            print("Phone number should be at least 7 digits.")
        except ValueError:
            print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, 1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, 1):
        print(f"{i}. {pizza}")

    return num_pizzas

def user_info():
    while True:
        option = input("Press 1 for delivery, Press 2 for pickup:\n\t")
        if option == "1":
            delivery_details()
            break
        elif option == "2":
            pizza_list()
            break

def main():
    name = customer_name()
    phone = phone_number()
    user_info()

    print(f"\nCustomer Name: {name}")
    print(f"Phone Number: {phone}")

main()

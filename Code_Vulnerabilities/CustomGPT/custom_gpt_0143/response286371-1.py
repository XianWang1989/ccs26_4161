
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

user_info = {}

def customer_name():
    while True:
        customer_name = input("Please enter your name: ")
        if customer_name:
            user_info['name'] = customer_name
            break
        else:
            print("Error: you must enter a valid name.")

def delivery_details():
    while True:
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address:
            user_info['address'] = delivery_address
            break
        else:
            print("Error: you must enter a valid address.")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number: "))
            if 1000000 <= phone <= 9999999:  # Example: must be 7 digits
                user_info['phone'] = phone
                break
            else:
                print("Phone number must be a 7 digit integer.")
        except ValueError:
            print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input("How many pizzas would you like (max of 5): "))
        except ValueError:
            print("Invalid input.")

    user_info['num_pizzas'] = num_pizzas
    selected_pizzas = []

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    # Collect selected pizzas
    for _ in range(num_pizzas):
        while True:
            selected = input('Select a pizza (enter number): ')
            if selected.isdigit() and 1 <= int(selected) <= len(premium_pizzas + gourmet_pizzas):
                selected_pizzas.append(selected)
                break
            else:
                print("Invalid selection.")

    user_info['selected_pizzas'] = selected_pizzas

def main():
    customer_name()
    phone_number()
    delivery_details()
    pizza_list()

    print("\n--- User Information ---")
    for key, value in user_info.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    main()

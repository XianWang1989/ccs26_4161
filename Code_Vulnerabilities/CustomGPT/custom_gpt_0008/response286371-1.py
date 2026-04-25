
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    customer_name = ""
    while customer_name == "":
        try:
            customer_name = input("Please enter your name: ")
            if customer_name.isdigit():
                raise ValueError("Name cannot be a number.")
        except ValueError as e:
            print(e)

    return customer_name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = input("Please enter your delivery address: ")
        except Exception:
            print("Error: you must enter something!")

    return delivery_address

def phone_input():
    phone_number = ""
    while len(phone_number) < 7 or not phone_number.isdigit():
        phone_number = input("Please enter your phone number (at least 7 digits): ")
        if len(phone_number) < 7 or not phone_number.isdigit():
            print("Valid phone number is required.")

    return phone_number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input, must be a number.')

    # For simplicity, just print the choices
    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")
    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery, press 2 for pickup: ")
        if get_user_info == "1":
            delivery_address = delivery_details()
            break
        elif get_user_info == "2":
            print("Pickup selected.")
            break
        else:
            print("Invalid input, please try again.")

def main():
    name = customer_name()
    phone = phone_input()
    user_info()
    print(f"\nCustomer Name: {name}\nPhone Number: {phone}")

# Start the program
main()

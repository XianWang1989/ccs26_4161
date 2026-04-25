
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

def customer_name():
    customer_name = ""
    while not customer_name:
        customer_name = input("Please enter your name: ")
    return customer_name

def delivery_details():
    delivery_address = ""
    while not delivery_address:
        delivery_address = input("Please enter your delivery address: ")
    return delivery_address

def phone_number_input():
    phone_number = -1
    while phone_number < 0 or phone_number < 7:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
        except ValueError:
            print("Phone number must be an integer.")
    return phone_number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')
            continue

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, 1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, 1):
        print(f"{i}. {pizza}")

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number_input()
    pizza_list()

    print(f"\nUser Information:\nName: {name}\nAddress: {address}\nPhone: {phone}")

main()

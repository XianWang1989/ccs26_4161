
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

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

def phone_number():
    phone = -1
    while phone < 0 or phone < 7:
        try:
            phone = int(input("Please enter your phone number:\n"))
        except ValueError:
            print("Phone number must be an integer only.")
    return phone

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    pizza_dict = {
        "premium_pizza_price": 8.50,
        "gourmet_pizza_price": 5.00,
        "num_premium_pizzas": 0,
        "num_gourmet_pizzas": 0
    }

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, 1):
        print(f'{i}. {pizza}')

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, 1):
        print(f'{i}. {pizza}')

    return pizza_dict

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number()
    pizza_dict = pizza_list()

    # Collecting all user info in a list
    receipt = [name, address, phone, pizza_dict]

    print("\nUser Details:")
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Phone: {phone}")
    # Print pizza information from `pizza_dict` if needed
    print(f"Premium Pizzas Ordered: {pizza_dict['num_premium_pizzas']}")
    print(f"Gourmet Pizzas Ordered: {pizza_dict['num_gourmet_pizzas']}")

if __name__ == "__main__":
    main()

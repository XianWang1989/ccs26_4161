
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
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
        try:
            name = str(input("Please enter your name: "))
            if not name.isalpha():
                raise ValueError("Name cannot contain numbers.")
        except ValueError as e:
            print(f"Error: {e}")
    return name

def delivery_details():
    address = ""
    while address == "":
        try:
            address = str(input("Please enter your delivery address: "))
        except ValueError:
            print("Error: you must enter something!")
    return address

def phone_number():
    number = 0
    while number < 1000000 or number >= 10000000:
        try:
            number = int(input("Please enter your phone number (7 digits): "))
            if number < 1000000 or number >= 10000000:
                print("Phone number must be 7 digits only.")
        except ValueError:
            print("Phone number must be an integer.")
    return number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input.')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    # Process premium pizzas
    for _ in range(num_pizzas):
        selected = int(input('Select Your Premium Pizza (or enter 0 to skip): '))
        if selected > 0 and selected <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1

    # Process gourmet pizzas
    for _ in range(num_pizzas):
        selected = int(input('Select Your Gourmet Pizza (or enter 0 to skip): '))
        if selected > 0 and selected <= len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1

def main():
    name = customer_name()
    number = phone_number()
    address = delivery_details()
    pizza_list()

    print(f"\nCustomer Name: {name}")
    print(f"Phone Number: {number}")
    print(f"Delivery Address: {address}")
    print(f"Total Premium Pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Total Gourmet Pizzas: {pizza_dict['num_gourmet_pizzas']}")

if __name__ == "__main__":
    main()

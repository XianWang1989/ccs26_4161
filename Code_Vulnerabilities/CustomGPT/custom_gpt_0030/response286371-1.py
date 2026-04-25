
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
            name = input("Please enter your name: ")
            if any(char.isdigit() for char in name):
                raise ValueError("Name cannot contain numbers")
        except ValueError as e:
            print(e)
    return name

def delivery_details():
    address = ""
    while address == "":
        address = input("Please enter your delivery address: ")
    return address

def phone_number():
    num = -1
    while num < 0 or len(str(num)) < 7:
        try:
            num = int(input("Please enter your phone number (at least 7 digits): "))
            if len(str(num)) < 7:
                raise ValueError("Phone number must be at least 7 digits.")
        except ValueError as e:
            print(e)
    return num

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for i, pizza in enumerate(premium_pizzas):
        print(f"{i + 1}. {pizza}")

    print('\nSelect your premium pizzas:')
    for _ in range(num_pizzas):
        try:
            selected = int(input('Select your Premium Pizza (enter number): '))
            if 1 <= selected <= len(premium_pizzas):
                pizza_dict['num_premium_pizzas'] += 1
            else:
                print('Invalid selection')
        except ValueError:
            print('Invalid Input')

    # Repeat for gourmet pizzas similarly
    for i, pizza in enumerate(gourmet_pizzas):
        print(f"{i + 1}. {pizza}")

    print('\nSelect your gourmet pizzas:')
    for _ in range(num_pizzas):
        try:
            selected = int(input('Select your Gourmet Pizza (enter number): '))
            if 1 <= selected <= len(gourmet_pizzas):
                pizza_dict['num_gourmet_pizzas'] += 1
            else:
                print('Invalid selection')
        except ValueError:
            print('Invalid Input')

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number()
    pizza_list()

    print(f"\nReceipt for {name}:\n")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {phone}")
    print(f"Total Premium Pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Total Gourmet Pizzas: {pizza_dict['num_gourmet_pizzas']}")
    total_cost = (pizza_dict["num_premium_pizzas"] * pizza_dict['premium_pizza_price']) + (pizza_dict["num_gourmet_pizzas"] * pizza_dict['gourmet_pizza_price'])
    print(f"Total Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()

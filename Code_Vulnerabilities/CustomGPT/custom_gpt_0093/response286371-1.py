
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    name = ""
    while name == "":
        try:
            name = input("Please enter your name: ")
            if name.isdigit():  # Ensure name isn't numeric
                raise ValueError("Name cannot be a number.")
        except ValueError as e:
            print(e)
    return name

def delivery_details():
    address = ""
    while address == "":
        try:
            address = input("Please enter your delivery address: ")
            if not address:
                raise ValueError("Address cannot be empty.")
        except ValueError as e:
            print(e)
    return address

def phone_number():
    number = ""
    while not (number.isdigit() and len(number) >= 7):
        number = input("Please enter your phone number (at least 7 digits): ")
    return number

def pizza_list(num_pizzas):
    pizza_dict = {"num_premium_pizzas": 0, "num_gourmet_pizzas": 0}
    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas):
        print(f"{i + 1}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas):
        print(f"{i + 1}. {pizza}")

    for _ in range(num_pizzas):
        selected = int(input("Select Your Premium Pizza (1-{}): ".format(len(premium_pizzas))))
        if 1 <= selected <= len(premium_pizzas):
            pizza_dict["num_premium_pizzas"] += 1

    for _ in range(num_pizzas):
        selected = int(input("Select Your Gourmet Pizza (1-{}): ".format(len(gourmet_pizzas))))
        if 1 <= selected <= len(gourmet_pizzas):
            pizza_dict["num_gourmet_pizzas"] += 1

    return pizza_dict

def main():
    name = customer_name()
    num_pizzas = int(input("How many pizzas would you like (max of 5): "))
    if num_pizzas > 5:
        num_pizzas = 5  # Limit number of pizzas

    pizza_dict = pizza_list(num_pizzas)
    address = delivery_details()
    number = phone_number()

    print(f"\nCustomer Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {number}")
    print(f"Total Premium Pizzas Ordered: {pizza_dict['num_premium_pizzas']}")
    print(f"Total Gourmet Pizzas Ordered: {pizza_dict['num_gourmet_pizzas']}")

main()

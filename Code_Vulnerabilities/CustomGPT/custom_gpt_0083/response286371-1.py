
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.isdigit():
                raise ValueError("Name cannot be a number!")
            return name
        except ValueError as e:
            print(e)

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address == "":
                raise ValueError("Address must not be empty!")
            return address
        except ValueError as e:
            print(e)

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
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
    for index, pizza in enumerate(premium_pizzas, start=1):
        print(f"{index}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for index, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{index}. {pizza}")

    return num_pizzas, pizza_dict

def user_info():
    while True:
        choice = input("Press 1 for delivery, Press 2 for pickup: ")
        if choice == "1":
            delivery_details()
            return
        elif choice == "2":
            return

def main():
    name = customer_name()
    print(f"Customer Name: {name}")
    user_info()
    num_pizzas, pizza_dict = pizza_list()

    # Optional: Print summary
    print(f"Total pizzas ordered: {num_pizzas}")
    print(f"Pizza Pricing: Premium - {pizza_dict['premium_pizza_price']}, Gourmet - {pizza_dict['gourmet_pizza_price']}")

# Run the main function
if __name__ == "__main__":
    main()

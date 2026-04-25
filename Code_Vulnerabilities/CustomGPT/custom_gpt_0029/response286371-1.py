
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme",
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if not name.strip():
                raise ValueError("Name cannot be empty.")
            break
        except ValueError as e:
            print(e)

    return name

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if not address.strip():
                raise ValueError("Address cannot be empty.")
            break
        except ValueError as e:
            print(e)

    return address

def phone_number():
    while True:
        try:
            number = int(input("Please enter your phone number:\n\t"))
            if number < 1000000:  # Example validation for phone numbers
                raise ValueError("Phone number must have at least 7 digits.")
            break
        except ValueError as e:
            print(e)

    return number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if num_pizzas < 1 or num_pizzas > 5:
                raise ValueError("Please enter a valid number of pizzas.")
        except ValueError as e:
            print(e)

    # Further pizza selection logic...
    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    # Similar for gourmet pizzas...

    return num_pizzas

def user_info():
    while True:
        choice = input("Press 1 for delivery or 2 for pickup: ")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            pizza_list()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def main():
    name = customer_name()
    number = phone_number()
    print(f"Customer Name: {name}, Phone Number: {number}")
    user_info()

if __name__ == "__main__":
    main()

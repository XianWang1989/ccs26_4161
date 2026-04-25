
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
        else:
            print("Error: You must enter something!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ").strip()
        if address:
            return address
        else:
            print("Error: You must enter something!")

def phone_number():
    while True:
        try:
            number = int(input("Please enter your phone number (digits only): "))
            if number >= 1000000:  # simple check for valid phone number.
                return number
            else:
                print("Phone number must be at least 7 digits.")
        except ValueError:
            print("Error: Phone number must be integer only.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    selected_pizzas = []
    for _ in range(num_pizzas):
        selection = int(input('Select Your Premium Pizza (1-7) or "0" to finish: '))
        if selection == 0:
            break
        if 1 <= selection <= len(premium_pizzas):
            selected_pizzas.append(premium_pizzas[selection - 1])
        else:
            print("Invalid input!")

    return selected_pizzas

def main():
    name = customer_name()
    address = delivery_details()
    number = phone_number()
    pizzas = pizza_list()

    print("\nThank you, here is your order:")
    print(f"Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {number}")
    print(f"Selected Pizzas: {', '.join(pizzas)}")

if __name__ == "__main__":
    main()

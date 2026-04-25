
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "selected_pizzas": 0,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name.isalpha() and name:
            return name
        print("Error: You must enter a valid name!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        print("Error: You must enter an address!")

def phone_number():
    while True:
        try:
            number = int(input("Please enter your phone number (digits only): "))
            if number > 999999 and number < 10000000:  # Example: validating 7-digit phone numbers
                return number
        except ValueError:
            pass
        print("Error: Phone number must be a 7-digit integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:  # Max pizzas allowed: 5
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            pass
        print('Invalid Input')

    for i in range(len(premium_pizzas)):
        print(str(i + 1) + '. ' + premium_pizzas[i])
    for i in range(len(gourmet_pizzas)):
        print(str(i + 1) + '. ' + gourmet_pizzas[i])

    selected_pizzas = []
    for _ in range(num_pizzas):
        selected = int(input('Select Your Pizza by number (1 for premium, 2 for gourmet): '))
        selected_pizzas.append(selected)
    return selected_pizzas

def main():
    name = customer_name()
    phone = phone_number()
    address = delivery_details()
    selected_pizzas = pizza_list()

    print(f"Customer Name: {name}")
    print(f"Phone Number: {phone}")
    print(f"Delivery Address: {address}")
    print(f"Selected Pizzas: {selected_pizzas}")

if __name__ == "__main__":
    main()


premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name:
            return name
        print("Error! You must enter a name.")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        print("Error! You must enter an address.")

def phone_number():
    while True:
        try:
            num = int(input("Please enter your phone number: "))
            if num >= 1000000:  # Assuming phone numbers are >= 7 digits
                return num
        except ValueError:
            print("Error! Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for i in range(1, len(premium_pizzas) + 1):
        print(f'{i}. {premium_pizzas[i - 1]}')

    # Other pizza selection logic can go here...

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number()
    pizza_list()

    print(f"\nThank you, {name}! We will deliver to {address} and call you at {phone}.")

if __name__ == "__main__":
    main()

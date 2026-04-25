
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
        name = input("Please enter your name: ")
        if name.isalpha():
            return name
        else:
            print("Error: Name cannot be a number or empty!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        else:
            print("Error: Address cannot be empty!")

def phone_number():
    while True:
        try:
            number = int(input("Please enter your phone number (digits only): "))
            if len(str(number)) >= 7:
                return number
            else:
                print("Phone number must be at least 7 digits.")
        except ValueError:
            print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while not (0 < num_pizzas <= 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):  # Loop through selected pizzas
        selected = -1
        while not (1 <= selected <= len(premium_pizzas)):
            try:
                selected = int(input('Select Your Premium Pizza by number: '))
                if 1 <= selected <= len(premium_pizzas):
                    pizza_dict['num_premium_pizzas'] += 1
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

    print("Pizza selection complete")

def user_info():
    user_input = ""
    while user_input not in ["1", "2"]:
        user_input = input("Press 1 for delivery\nPress 2 for pickup: ")
    if user_input == "1":
        delivery_details()
    elif user_input == "2":
        pizza_list()

# Main Program
name = customer_name()
phone = phone_number()
user_info()
print(f"\nThank you, {name}. Your phone number is {phone}.")
print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")

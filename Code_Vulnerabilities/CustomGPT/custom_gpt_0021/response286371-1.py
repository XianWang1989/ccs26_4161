
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
        name = input("Please enter your name: ")
        if name and not name.isdigit():
            print(f"Welcome, {name}!")
            return name
        else:
            print("Error: Name cannot be empty or a number!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            print(f"Delivery address set to: {address}")
            return address
        else:
            print("Error: Address cannot be empty!")

def phone_number():
    while True:
        try:
            number = int(input("Please enter your phone number (digits only): "))
            if len(str(number)) >= 7:  # Simple check for minimum length
                return number
            else:
                print("Error: Phone number must be at least 7 digits!")
        except ValueError:
            print("Error: Phone number must be an integer!")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i+1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i+1}. {gourmet_pizzas[i]}")

    select_pizzas(num_pizzas)

def select_pizzas(num_pizzas):
    for _ in range(num_pizzas):
        while True:
            selected = input('Select Your Premium Pizza (enter "next" to move on): ')
            if selected == 'next':
                break
            try:
                selected = int(selected)
                if 1 <= selected <= len(premium_pizzas):
                    pizza_dict['num_premium_pizzas'] += 1
                    print(f"You selected: {premium_pizzas[selected - 1]}")
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

def user_info():
    while True:
        choice = input("Press 1 for delivery, Press 2 for pickup: ")
        if choice == "1":
            delivery_details()
            return
        elif choice == "2":
            print("You chose pickup.")
            return
        else:
            print("Invalid input, please enter 1 or 2.")

def main():
    name = customer_name()
    phone = phone_number()
    user_info()
    pizza_list()
    print(f"\nCustomer Name: {name}, Phone Number: {phone}")
    print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")

main()

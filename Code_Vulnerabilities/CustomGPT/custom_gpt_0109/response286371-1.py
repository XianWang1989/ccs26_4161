
premium_pizzas = [
    "Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme",
    "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"
]

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
        else:
            print("Error: You must enter a name!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        else:
            print("Error: You must enter a delivery address!")

def phone_number():
    while True:
        try:
            number = int(input("Please enter your phone number:\n\t"))
            if len(str(number)) >= 7:
                return number
            else:
                print("Phone number must be at least 7 digits.")
        except ValueError:
            print("Error: Phone number must be an integer!")

def pizza_selection():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for pizza_type, pizzas in [("Premium", premium_pizzas), ("Gourmet", gourmet_pizzas)]:
        print(f'\n=={pizza_type} Pizzas==\n')
        for i, pizza in enumerate(pizzas, start=1):
            print(f"{i}. {pizza}")

        for _ in range(num_pizzas):
            while True:
                selected = input(f'Select Your {pizza_type} Pizza (or enter "next" to move on): ')
                if selected.lower() == 'next':
                    break
                try:
                    selected = int(selected)
                    if 1 <= selected <= len(pizzas):
                        pizza_dict[f'num_{pizza_type.lower()}_pizzas'] += 1
                        break
                    else:
                        print('Invalid Input')
                except ValueError:
                    print('Invalid Input')

def user_info():
    while True:
        choice = input("Press 1 for delivery, 2 for pickup: ")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            print("Pickup selected.")
            break
        else:
            print("Invalid choice, please select 1 or 2.")

# Main execution
name = customer_name()
phone = phone_number()
user_info()
pizza_selection()

# Display final receipt details
print(f'\nCustomer Name: {name}')
print(f'Phone Number: {phone}')
print(f'Total number of premium pizzas: {pizza_dict["num_premium_pizzas"]}')
print(f'Total number of gourmet pizzas: {pizza_dict["num_gourmet_pizzas"]}')

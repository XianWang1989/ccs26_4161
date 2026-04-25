
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", 
                  "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", 
                  "BBQ Chicken", "Hellfire"]

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
            if not name.isalpha():
                raise ValueError("Name cannot be a number.")
            return name
        except ValueError as e:
            print(e)

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if not address:
                raise ValueError("Address cannot be empty.")
            return address
        except ValueError as e:
            print(e)

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number: "))
            if phone < 1000000:  # Simple check for phone number length
                raise ValueError("Phone number must be at least 7 digits.")
            return phone
        except ValueError as e:
            print(e)

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    # Collect selected premium pizzas
    for _ in range(num_pizzas):
        selected = int(input('Select Your Premium Pizza (enter number): '))
        if 1 <= selected <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1
        else:
            print("Invalid selection.")

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    # Collect selected gourmet pizzas
    for _ in range(num_pizzas):
        selected = int(input('Select Your Gourmet Pizza (enter number): '))
        if 1 <= selected <= len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1
        else:
            print("Invalid selection.")

def get_user_info():
    while True:
        user_choice = input("Press 1 for delivery, 2 for pickup: ")
        if user_choice == "1":
            delivery_details()
            break
        elif user_choice == "2":
            pizza_list()
            break
        else:
            print("Invalid choice.")

# Main program flow
name = customer_name()
phone = phone_number()
get_user_info()

# Print out the receipt
print(f"Customer Name: {name}")
print(f"Phone Number: {phone}")
print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")

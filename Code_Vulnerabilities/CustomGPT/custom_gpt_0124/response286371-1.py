
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
        try:
            name = input("Please enter your name: ")
            if name.isdigit():
                raise ValueError("Name cannot be a number.")
            return name
        except ValueError as e:
            print(e)

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        print("Error: must enter an address.")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number: "))
            if phone < 1000000 or phone > 9999999:  # Ensure it's a valid 7-digit number
                raise ValueError
            return phone
        except ValueError:
            print("Phone number must be a 7-digit integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
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

    return num_pizzas

def user_info():
    while True:
        choice = input("Press 1 for delivery or 2 for pickup: ")
        if choice == "1":
            delivery_details()
            return "Delivery selected."
        elif choice == "2":
            return "Pickup selected."
        else:
            print("Invalid choice. Please try again.")

# Main Program Flow
name = customer_name()
phone = phone_number()
pizzas_ordered = pizza_list()
info_choice = user_info()

# Print collected info
print(f"\nCustomer Name: {name}\nPhone Number: {phone}\nPizzas Ordered: {pizzas_ordered}\nInfo Choice: {info_choice}")

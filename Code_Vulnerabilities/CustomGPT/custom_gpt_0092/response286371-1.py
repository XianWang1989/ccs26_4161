
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
                   "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", 
                   "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
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
            if not name.isalpha():  # Ensure name contains only letters
                raise ValueError("Name must not contain numbers.")
            return name
        except ValueError as e:
            print(e)

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address.strip() == "":
                raise ValueError("Address cannot be empty.")
            return address
        except ValueError as e:
            print(e)

def phone_number_input():
    while True:
        try:
            number = int(input("Please enter your phone number:\n\t"))
            if number < 1000000:  # Assuming a 7-digit phone number
                raise ValueError("Phone number must be at least 7 digits.")
            return number
        except ValueError as e:
            print(e)

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input. Please enter a number.')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    return num_pizzas

def user_info():
    while True:
        choice = input("Press 1 for delivery, 2 for pickup:\n\t")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            pizza_list()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Main execution flow
customer_name_result = customer_name()
phone_number_result = phone_number_input()
user_info()

print(f"\nCustomer Name: {customer_name_result}")
print(f"Phone Number: {phone_number_result}")

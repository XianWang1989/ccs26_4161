
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme",
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ",
    "BBQ Chicken", "Hellfire"
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
        if name.strip() != "":
            return name
        print("Error: You must enter a valid name!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address.strip() != "":
            return address
        print("Error: You must enter a valid address!")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number: "))
            if phone >= 1000000:  # Assuming at least 7 digits
                return phone
            print("Error: Phone number must be 7 or more digits.")
        except ValueError:
            print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    return num_pizzas

def user_info():
    while True:
        option = input("Press 1 for delivery, 2 for pickup: ")
        if option == "1":
            delivery_details()
            break
        elif option == "2":
            pizza_list()
            break
        print("Invalid choice. Please try again.")

# Main flow
print("Welcome to the Pizza Ordering System!")
name = customer_name()
phone = phone_number()
user_info()

# Print results
print(f"\nCustomer Name: {name}\nPhone Number: {phone}")

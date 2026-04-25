
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

customer_info = {}

def customer_name():
    while True:
        customer_name = input("Please enter your name: ")
        if customer_name:
            customer_info['name'] = customer_name
            break
        else:
            print("Error: You must enter a name!")

def delivery_details():
    while True:
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address:
            customer_info['address'] = delivery_address
            break
        else:
            print("Error: You must enter an address!")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number: "))
            if phone > 0:
                customer_info['phone'] = phone
                break
            else:
                print("Phone number must be positive!")
        except ValueError:
            print("Phone number must be an integer!")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    # Pizza selection logic can be added here

def user_info():
    while True:
        choice = input("Press 1 for delivery, Press 2 for pickup: ")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            pizza_list()
            break

# Main flow
customer_name()
phone_number()
user_info()

print(f"Customer Info: {customer_info}")

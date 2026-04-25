
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
    name = ""
    while name == "":
        name = input("Please enter your name: ")
    return name

def delivery_details():
    address = ""
    while address == "":
        address = input("Please enter your delivery address: ")
    return address

def phone_number():
    phone = -1
    while phone < 0 or phone < 7:
        try:
            phone = int(input("Please enter your phone number:\n\t"))
        except ValueError:
            print("Phone number must be an integer only.")
    return phone

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f'{i}. {pizza}')

    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f'{i}. {pizza}')

def user_info():
    while True:
        choice = input("Press 1 for delivery, press 2 for pickup:\n\t")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            pizza_list()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Main execution flow
name = customer_name()
phone = phone_number()
user_info()

# Print summary
print(f"Customer Name: {name}, Phone Number: {phone}")

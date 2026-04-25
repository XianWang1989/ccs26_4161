
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
            if not name.isalpha():
                raise ValueError("Name cannot contain numbers.")
            return name
        except ValueError as e:
            print("Error:", e)

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
            phone = int(input("Please enter your phone number:\n\t"))
            if phone < 1000000:  # Example condition for phone validation
                raise ValueError("Phone number too short.")
            return phone
        except ValueError as e:
            print("Error:", e)

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5):'))
        except ValueError:
            print('Invalid Input')

    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i + len(premium_pizzas)}. {pizza}")

    return num_pizzas

def user_info():
    while True:
        try:
            choice = input("Press 1 for delivery, Press 2 for pickup:\n")
            if choice == '1':
                delivery_details()
                break
            elif choice == '2':
                pizza_list()
                break
            else:
                print("Invalid Choice")
        except Exception as e:
            print("Error:", e)

# Main Execution
name = customer_name()
phone = phone_number()
user_info()

print(f"Customer Name: {name}, Phone: {phone}")

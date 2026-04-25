
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
    name = ""
    while name == "":
        try:
            name = str(input("Please enter your name: "))
            return name
        except:
            print("Error: You must enter something!")

def delivery_details():
    address = ""
    while address == "":
        try:
            address = str(input("Please enter your delivery address: "))
            return address
        except:
            print("Error: You must enter something!")

def phone_number():
    phone = -1
    while phone < 0 or phone < 7:
        try:
            phone = int(input("Please enter your phone number (7 digits minimum): "))
            return phone
        except:
            print("Error: Phone number must be an integer and at least 7 digits long.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except:
            print('Invalid Input')

    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    return num_pizzas

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery, press 2 for pickup: ")
        if get_user_info == "1":
            delivery_details()
        elif get_user_info == "2":
            pizza_list()
        else:
            print("Invalid choice!")

# Main execution
name = customer_name()
phone = phone_number()
pizza_count = pizza_list()

print(f"Customer Name: {name}")
print(f"Phone Number: {phone}")
print(f"Number of Pizzas: {pizza_count}")

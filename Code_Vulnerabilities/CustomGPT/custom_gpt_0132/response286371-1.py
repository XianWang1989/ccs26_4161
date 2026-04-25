
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name:
            return name
        print("Error: You must enter a name!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        print("Error: You must enter an address!")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if phone_number > 0:  # Ensure phone number is positive
                return phone_number
        except ValueError:
            print("Phone number must be an integer!")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (1-5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")
    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    # More pizza selection logic can go here...

def user_info():
    option = ""
    while option not in ["1", "2"]:
        option = input("Press 1 for delivery or 2 for pickup: ")
    if option == "1":
        delivery_details()
    else:
        pizza_list()

# Main Program
name = customer_name()
phone_number = get_phone_number()
# You can then call user_info() if needed
user_info()

# Print collected information
print(f"Customer Name: {name}, Phone: {phone_number}")

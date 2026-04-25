
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", 
                  "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50, 
    "gourmet_pizza_price": 5.00, 
    "num_premium_pizzas": 0, 
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name.strip():
            return name
        print("Error: You must enter a valid name.")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address.strip():
            return address
        print("Error: You must enter a valid address.")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number:\n\t"))
            if len(str(phone)) >= 7:  # Ensure phone number has at least 7 digits
                return phone
            print("Phone number must have at least 7 digits.")
        except ValueError:
            print("Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    # Pizza selection logic
    for i in range(num_pizzas):
        # Premium Pizza Selection
        print('\n==Premium Pizzas==\n')
        for idx, pizza in enumerate(premium_pizzas, start=1):
            print(f"{idx}. {pizza}")
        premium_choice = int(input('Select Your Premium Pizza: '))
        pizza_dict['num_premium_pizzas'] += 1

        # Gourmet Pizza Selection
        print('\n==Gourmet Pizzas==\n')
        for idx, pizza in enumerate(gourmet_pizzas, start=1):
            print(f"{idx}. {pizza}")
        gourmet_choice = int(input('Select Your Gourmet Pizza: '))
        pizza_dict['num_gourmet_pizzas'] += 1

def user_info():
    choice = input("Press 1 for delivery or 2 for pickup: ")
    if choice == "1":
        delivery_details()
    elif choice == "2":
        print("Pickup selected.")

# Main execution
name = customer_name()
phone = phone_number()
pizza_list()  # Call to start pizza ordering process

# Print user details
print(f"\nCustomer Name: {name}")
print(f"Phone Number: {phone}")
print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")

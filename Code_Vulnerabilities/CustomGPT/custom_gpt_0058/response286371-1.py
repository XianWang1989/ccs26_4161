
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

# Storage for user info
user_info_dict = {}

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.isalpha():  # Ensuring the name is not a number
                user_info_dict['name'] = name
                break
            else:
                print("Error: Name must be alphabetic.")
        except Exception as e:
            print(f"Error: {e}")

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address:
                user_info_dict['address'] = address
                break
            else:
                print("Error: Address cannot be empty.")
        except Exception as e:
            print(f"Error: {e}")

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input. Please enter an integer.')

    # Continue with pizza selection as you had...

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery, Press 2 for pickup: ")
        if get_user_info == "1":
            delivery_details()
            break
        elif get_user_info == "2":
            pizza_list()
            break

# Collect user name first and then proceed
customer_name()
user_info()
# Print out the final information collected if needed
print(user_info_dict)  # Displaying collected user information

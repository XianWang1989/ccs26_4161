
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

user_info_list = []

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name.isalpha():  # Ensure the name contains only letters
            user_info_list.append(name)
            break
        print("Error: Name must contain only letters.")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            user_info_list.append(address)
            break
        print("Error: Address cannot be empty.")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number: "))
            if phone > 0:  # Ensure phone number is positive
                user_info_list.append(phone)
                break
        except ValueError:
            print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    # Logic to select pizzas could be added here...

def user_info():
    while True:
        choice = input("Press 1 for delivery or 2 for pickup: ")
        if choice == "1":
            delivery_details()
        elif choice == "2":
            pizza_list()
        else:
            print("Invalid choice.")

# Main code execution
customer_name()
phone_number()
user_info()  # Call the user_info function last

print("User Information:", user_info_list)  # Print collected user information

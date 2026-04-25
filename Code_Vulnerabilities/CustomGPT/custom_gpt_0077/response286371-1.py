
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
                  "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
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
        if name:
            return name
        else:
            print("Error: You must enter a name!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        else:
            print("Error: You must enter an address!")

def phone_number():
    while True:
        try:
            number = int(input("Please enter your phone number:\n"))
            if len(str(number)) >= 7:  # Adjust condition as per your requirement
                return number
        except ValueError:
            print("Phone number must be an integer!")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")
    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    for _ in range(num_pizzas):
        selected = int(input('Select Your Premium Pizza (or enter 0 to skip): '))
        if selected > 0 and selected <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1

    for _ in range(num_pizzas):
        selected = int(input('Select Your Gourmet Pizza (or enter 0 to skip): '))
        if selected > 0 and selected <= len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1

def user_info():
    while True:
        choice = input("Press 1 for delivery, press 2 for pickup: ")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            print("Pickup selected.")
            break
        else:
            print("Invalid choice! Please enter 1 or 2.")

# Main program flow
name = customer_name()
phone = phone_number()
user_info()
pizza_list()

# Display receipt (optional)
print(f"\nCustomer Name: {name}")
print(f"Phone Number: {phone}")
print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")

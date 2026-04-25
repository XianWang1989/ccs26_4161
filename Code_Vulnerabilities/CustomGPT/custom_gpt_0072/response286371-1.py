
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
    "Teeto shroomo supreme", "The volcanic rengar", 
    "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
    "BBQ Chicken", "Hellfire"
]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0,
    "total_cost": 0
}

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name.isalpha():  # Ensures name is valid
            return name
        else:
            print("Error: Name must not be a number or empty.")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        else:
            print("Error: Address cannot be empty.")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if len(str(phone_number)) >= 7:  # Checks if length is valid
                return phone_number
            else:
                print("Phone number must be at least 7 digits.")
        except ValueError:
            print("Phone number must be an integer only.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    # Collect premium pizzas
    for _ in range(num_pizzas):
        selected = int(input('Select Your Premium Pizza (or type "next" to move on): '))
        if 1 <= selected <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1
        else:
            print('Invalid Input')

    # Collect gourmet pizzas
    for _ in range(num_pizzas):
        selected = int(input('Select Your Gourmet Pizza (or type "next" to move on): '))
        if 1 <= selected <= len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1
        else:
            print('Invalid Input')

def user_info():
    user_choice = input("Press 1 for delivery or 2 for pickup: ")
    if user_choice == "1":
        delivery_details()
    elif user_choice == "2":
        pizza_list()

# Main program flow
name = customer_name()
phone_number = get_phone_number()
user_info()

# Print out the summary
print(f"\nReceipt for {name} (Phone: {phone_number}):")
print(f"Total Premium Pizzas: {pizza_dict['num_premium_pizzas']}")
print(f"Total Gourmet Pizzas: {pizza_dict['num_gourmet_pizzas']}")
# Here you can add to calculate total cost if needed

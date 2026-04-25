
premium_pizzas = [
    "Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme",
    "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ",
    "BBQ Chicken", "Hellfire"
]

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
            phone = int(input("Please enter your phone number (digits only): "))
            if phone >= 1000000:  # Assuming phone number should have at least 7 digits
                return phone
            else:
                print("Phone number must be at least 7 digits")
        except ValueError:
            print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while(num_pizzas < 0 or num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for _ in range(num_pizzas):
        # Select premium pizzas
        while True:
            selected = input('Select Your Premium Pizza (or "next" to skip): ')
            if selected == 'next':
                break
            try:
                selected = int(selected)
                if 0 < selected <= len(premium_pizzas):
                    pizza_dict['num_premium_pizzas'] += 1
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

        # Select gourmet pizzas
        while True:
            selected = input('Select Your Gourmet Pizza (or "next" to skip): ')
            if selected == 'next':
                break
            try:
                selected = int(selected)
                if 0 < selected <= len(gourmet_pizzas):
                    pizza_dict['num_gourmet_pizzas'] += 1
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery, 2 for pickup: ")
        if get_user_info == "1":
            delivery_details()
            break
        elif get_user_info == "2":
            pizza_list()
            break
        else:
            print("Invalid choice.")

# Main Execution Flow
name = customer_name()
phone = phone_number()
user_info()

# Finally, display the user's info
print(f"Name: {name}")
print(f"Phone: {phone}")
print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")


premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
                  "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
                  "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.isalpha():  # Ensure name contains only letters
                return name
            else:
                print("Error: Name must contain only letters.")
        except Exception as e:
            print("Error:", e)

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address:
                return address
            else:
                print("Error: Address cannot be empty.")
        except Exception as e:
            print("Error:", e)

def get_phone_number():
    while True:
        try:
            phone_number = input("Please enter your phone number (digits only): ")
            if phone_number.isdigit() and len(phone_number) >= 7:
                return phone_number
            else:
                print("Phone number must be at least 7 digits long.")
        except Exception as e:
            print("Error:", e)

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, 1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, 1):
        print(f"{i}. {pizza}")

    # Select pizzas
    for pizza_type in ['premium', 'gourmet']:
        while num_pizzas > 0:
            selected = input(f'Select Your {pizza_type.capitalize()} Pizza (or type "next" to finish): ')
            if selected == "next":
                break
            try:
                selected_index = int(selected) - 1
                if selected_index >= 0 and selected_index < len(premium_pizzas if pizza_type == 'premium' else gourmet_pizzas):
                    pizza_dict[f'num_{pizza_type}_pizzas'] += 1
                    num_pizzas -= 1
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

def user_info():
    while True:
        choice = input("Press 1 for delivery or 2 for pickup: ")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            pizza_list()
            break
        else:
            print("Invalid choice, please select again.")

# Main program execution
name = customer_name()
phone_number = get_phone_number()
user_info()

print(f"\nCustomer Name: {name}")
print(f"Phone Number: {phone_number}")
print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")

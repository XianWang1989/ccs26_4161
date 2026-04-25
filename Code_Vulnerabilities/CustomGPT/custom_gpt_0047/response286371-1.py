
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {"premium_pizza_price":8.50, "gourmet_pizza_price":5.00, "num_premium_pizzas":0, "num_gourmet_pizzas":0}

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name.isalpha():  # Ensure the name is not empty and contains only letters
            print(f"Welcome, {name}!")
            break
        else:
            print("Error: You must enter a valid name!")

def delivery_details():
    while True:
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address:
            print(f"Delivery address set to: {delivery_address}")
            break
        else:
            print("Error: You must enter a delivery address!")

def phone_number_input():
    while True:
        phone_number = input("Please enter your phone number (digits only): ")
        if phone_number.isdigit() and len(phone_number) >= 7:
            print(f"Phone number set to: {phone_number}")
            break
        else:
            print("Error: Phone number must be a valid integer of at least 7 digits.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        num_pizzas = int(input('How many pizzas would you like (max of 5): '))

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, 1):
        print(f"{i}. {pizza}")

    while num_pizzas > 0:
        selected = int(input('Select your Premium Pizza (or enter 0 to finish): '))
        if selected == 0:  # Allow user to finish early
            break
        if 1 <= selected <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1
            print(f"You selected: {premium_pizzas[selected - 1]}")
            num_pizzas -= 1
        else:
            print("Invalid Input")

    # Repeat for gourmet pizzas if there's still a need

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery, Press 2 for pickup: ")
        if get_user_info == "1":
            delivery_details()
            break
        elif get_user_info == "2":
            pizza_list()
            break
        else:
            print("Invalid choice, please enter 1 or 2.")

# Run the program
customer_name()
phone_number_input()
user_info()

# Final receipt information
print(f'\nTotal number of premium pizzas: {pizza_dict["num_premium_pizzas"]}')
# Add any other information you want to print here

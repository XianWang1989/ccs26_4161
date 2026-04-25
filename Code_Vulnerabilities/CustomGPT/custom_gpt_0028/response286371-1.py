
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

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
            if name.strip() == "":
                raise ValueError("Name cannot be empty")
            return name  # Return the customer name
        except ValueError as e:
            print(e)

def delivery_details():
    while True:
        try:
            delivery_address = input("Please enter your delivery address: ")
            if delivery_address.strip() == "":
                raise ValueError("Address cannot be empty")
            return delivery_address  # Return the delivery address
        except ValueError as e:
            print(e)

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number (digits only): "))
            if phone < 1000000:  # example check for valid phone number
                raise ValueError("Phone number must be at least 7 digits")
            return phone
        except ValueError as e:
            print(e)

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(str(i) + '. ' + pizza)

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(str(i) + '. ' + pizza)

    # Pizza selection
    for _ in range(num_pizzas):
        while True:
            selected = input('Select Your Premium Pizza (or type "next" to move on): ')
            if selected.lower() == "next":
                break
            try:
                selected = int(selected)
                if selected < 1 or selected > len(premium_pizzas):
                    print('Invalid Input')
                else:
                    pizza_dict['num_premium_pizzas'] += 1
                    break
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

# Main Execution
name = customer_name()
phone = phone_number()
user_info()

# Optional: Print out collected information
print(f"\nCustomer Name: {name}")
print(f"Phone Number: {phone}")
print(f"Total Premium Pizzas: {pizza_dict['num_premium_pizzas']}")
# Uncomment to show total cost if needed:
# cost = (pizza_dict["num_premium_pizzas"] * pizza_dict['premium_pizza_price'])
# print(f'Total cost: {cost}')

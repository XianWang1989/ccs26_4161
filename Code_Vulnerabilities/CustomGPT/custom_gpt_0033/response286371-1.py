
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "selected_pizzas": 0,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.isalpha():  # Ensure name doesn't contain numbers
                return name
            else:
                print("Name cannot contain numbers!")
        except Exception as e:
            print(f"Error: {e}")

def delivery_details():
    while True:
        try:
            delivery_address = input("Please enter your delivery address: ")
            if delivery_address:  # Check if input is not empty
                return delivery_address
            else:
                print("Address cannot be empty!")
        except Exception as e:
            print(f"Error: {e}")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number (digits only): "))
            if len(str(phone_number)) >= 7:  # Ensure phone number has at least 7 digits
                return phone_number
            else:
                print("Phone number must have at least 7 digits!")
        except ValueError:
            print("Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f'{i}. {pizza}')

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f'{i}. {pizza}')

    # Process pizza selection
    selected_pizzas = []
    while num_pizzas > 0:
        selected = input(f'Select Your Pizza (1-{len(premium_pizzas + gourmet_pizzas)}) or type "next" to finish: ')
        if selected.lower() == 'next':
            break
        try:
            selected = int(selected)
            if 1 <= selected <= len(premium_pizzas + gourmet_pizzas):
                selected_pizzas.append((selected, premium_pizzas[selected - 1] if selected <= len(premium_pizzas) else gourmet_pizzas[selected - len(premium_pizzas) - 1]))
                num_pizzas -= 1
            else:
                print('Invalid selection!')
        except ValueError:
            print('Invalid Input')

    return selected_pizzas

def user_info():
    user_choice = input("Press 1 for delivery, press 2 for pickup: ")
    if user_choice == "1":
        delivery_address = delivery_details()
        return delivery_address
    elif user_choice == "2":
        return "Pickup selected."

# Main Logic
name = customer_name()
phone_number = get_phone_number()
delivery_or_pickup = user_info()
selected_pizzas = pizza_list()

# Summary
print(f"\nCustomer Name: {name}")
print(f"Phone Number: {phone_number}")
print(f"Delivery Address: {delivery_or_pickup if delivery_or_pickup != 'Pickup selected.' else 'N/A'}")
print("Selected Pizzas:")
for pizza in selected_pizzas:
    print(f"- {pizza[1]}")

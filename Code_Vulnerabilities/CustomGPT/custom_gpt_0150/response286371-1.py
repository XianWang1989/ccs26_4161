
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", 
    "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
    "BBQ Chicken", "Hellfire"
]

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name.isalpha():
            return name
        else:
            print("Error! Name cannot be empty or a number.")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        else:
            print("Error! Address cannot be empty.")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number:\n\t"))
            if len(str(phone)) >= 7:
                return phone
            else:
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

    selected_pizzas = []
    for _ in range(num_pizzas):
        print('\n==Premium Pizzas==\n')
        for i, pizza in enumerate(premium_pizzas, start=1):
            print(f"{i}. {pizza}")

        selected = int(input('Select Your Premium Pizza (or enter 0 to skip): '))
        if selected > 0 and selected <= len(premium_pizzas):
            selected_pizzas.append(premium_pizzas[selected - 1])

    # Repeat for gourmet pizzas...
    # (You can add similar logic for gourmet pizzas if needed)

    return selected_pizzas

# Main flow to collect user information
name = customer_name()
address = delivery_details()
phone = phone_number()
pizzas = pizza_list()

# Print collected information
print("\nCollected Information:")
print(f"Name: {name}")
print(f"Address: {address}")
print(f"Phone: {phone}")
print(f"Selected Pizzas: {pizzas}")

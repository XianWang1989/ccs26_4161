
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    name = ""
    while name == "":
        try:
            name = input("Please enter your name: ")
        except ValueError:
            print("Error: You must enter something!")
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = input("Please enter your delivery address: ")
        except ValueError:
            print("Error: You must enter something!")
    return delivery_address

def phone_number():
    num = -1
    while num < 0 or len(str(num)) < 7:
        try:
            num = int(input("Please enter your phone number (at least 7 digits): "))
        except ValueError:
            print("Phone number must be an integer.")
    return num

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for i in range(len(premium_pizzas)):
        print(str(i + 1) + '. ' + premium_pizzas[i])
    for i in range(len(gourmet_pizzas)):
        print(str(i + 1) + '. ' + gourmet_pizzas[i])

    selected_pizzas = []
    for _ in range(num_pizzas):
        selected = int(input('Select your pizza (1 for premium, 2 for gourmet): '))
        if selected == 1:
            pizza_choice = int(input("Select Your Premium Pizza: "))
            pizza_dict['num_premium_pizzas'] += 1
        elif selected == 2:
            pizza_choice = int(input("Select Your Gourmet Pizza: "))
            pizza_dict['num_gourmet_pizzas'] += 1
        selected_pizzas.append(pizza_choice)

    return selected_pizzas

# Main execution flow
name = customer_name()
address = delivery_details()
phone = phone_number()
pizzas_ordered = pizza_list()

print("\n--- Receipt ---")
print(f"Customer Name: {name}")
print(f"Delivery Address: {address}")
print(f"Phone Number: {phone}")
print(f"Total Number of Premium Pizzas: {pizza_dict['num_premium_pizzas']}")
print(f"Total Number of Gourmet Pizzas: {pizza_dict['num_gourmet_pizzas']}")
total_cost = (pizza_dict['num_premium_pizzas'] * pizza_dict['premium_pizza_price']) + (pizza_dict['num_gourmet_pizzas'] * pizza_dict['gourmet_pizza_price'])
print(f"Total Cost: {total_cost}")

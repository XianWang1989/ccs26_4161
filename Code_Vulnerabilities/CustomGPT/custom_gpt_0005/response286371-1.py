
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50, 
    "gourmet_pizza_price": 5.00, 
    "num_premium_pizzas": 0, 
    "num_gourmet_pizzas": 0
}

def user_info():
    get_user_info = ""
    while get_user_info not in ["1", "2"]:
        get_user_info = input("Press 1 for delivery, press 2 for pickup: ")

    if get_user_info == "1":
        delivery_details()
    elif get_user_info == "2":
        pizza_list()

def customer_name():
    name = ""
    while not name:
        name = input("Please enter your name: ")
    return name

def delivery_details():
    delivery_address = ""
    while not delivery_address:
        delivery_address = input("Please enter your delivery address: ")

def phone_number():
    number = ""
    while not number.isdigit() or len(number) < 7:
        number = input("Please enter your phone number (at least 7 digits): ")
    return number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    selected_pizzas(num_pizzas)

def selected_pizzas(num_pizzas):
    for _ in range(num_pizzas):
        selected = input('Select Your Pizza (or type "next" to skip): ')
        if selected.lower() == 'next':
            break
        print(f"You selected pizza number {selected}.")  # Handle selection logic here

# Main execution
name = customer_name()
phone = phone_number()
user_info()

print(f"\nCustomer Name: {name}, Phone: {phone}")

# Note: Receipt generation and cost calculation can be added as needed.

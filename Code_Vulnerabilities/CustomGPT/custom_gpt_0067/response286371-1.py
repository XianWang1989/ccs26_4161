
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme",
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ",
    "BBQ Chicken", "Hellfire"
]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ")
        if name.strip() == "":
            print("Error: You must enter a name!")
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address.strip() == "":
            print("Error: You must enter an address!")
    return delivery_address

def phone_number():
    number = ""
    while len(number) < 7 or not number.isdigit():
        number = input("Please enter your phone number (at least 7 digits): ")
        if len(number) < 7 or not number.isdigit():
            print("Error: Phone number must be at least 7 digits long.")
    return number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for i in range(1, len(premium_pizzas) + 1):
        print(f"{i}. {premium_pizzas[i - 1]}")
    for i in range(1, len(gourmet_pizzas) + 1):
        print(f"{i}. {gourmet_pizzas[i - 1]}")

    selected_pizzas = []
    while len(selected_pizzas) < num_pizzas:
        selected = input('Select Your Premium Pizza (or type "next" to finish): ')
        if selected == "next":
            break
        try:
            selected = int(selected)
            if 1 <= selected <= len(premium_pizzas):
                selected_pizzas.append(premium_pizzas[selected - 1])
                pizza_dict['num_premium_pizzas'] += 1
            else:
                print('Invalid Input')
        except ValueError:
            print('Invalid Input')

    return selected_pizzas

def user_info():
    choice = ""
    while choice not in ["1", "2"]:
        choice = input("Press 1 for delivery, press 2 for pickup: ")
    if choice == "1":
        delivery_details()
    elif choice == "2":
        pizza_list()

# Main program
name = customer_name()
phone = phone_number()
user_info()

print(f"\nCustomer Name: {name}")
print(f"Phone Number: {phone}")
print(f"Number of Premium Pizzas: {pizza_dict['num_premium_pizzas']}")

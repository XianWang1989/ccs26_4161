
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

order_info = []  # To store user information

def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ")
    order_info.append(name)  # Save name to order info
    delivery_details()  # Call next function

def delivery_details():
    address = ""
    while address == "":
        address = input("Please enter your delivery address: ")
    order_info.append(address)  # Save address to order info
    phone_number()  # Call next function

def phone_number():
    phone = ""
    while len(phone) < 7:
        phone = input("Please enter your phone number (at least 7 digits): ")
        if not phone.isdigit() or len(phone) < 7:
            print("Phone number must be at least 7 digits.")
            phone = ""
    order_info.append(phone)  # Save phone to order info
    pizza_list()  # Call next function

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    order_info.append(num_pizzas)  # Save number of pizzas to order info

    print('\n==Premium Pizzas==')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    # Here you can call further selections of pizzas if needed

def display_receipt():
    print("\nYour Order Summary:")
    for info in order_info:
        print(info)

# Start the program
customer_name()
display_receipt()

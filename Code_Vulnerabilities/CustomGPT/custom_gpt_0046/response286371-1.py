
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
    name = ""
    while name == "":
        try:
            name = str(input("Please enter your name: "))
        except ValueError:
            print("Error: You must enter a name!")
    return name

def delivery_details():
    address = ""
    while address == "":
        try:
            address = str(input("Please enter your delivery address: "))
        except ValueError:
            print("Error: You must enter an address!")
    return address

def get_phone_number():
    phone_number = -1
    while phone_number < 0 or len(str(phone_number)) < 7:
        try:
            phone_number = int(input("Please enter your phone number (at least 7 digits): "))
        except ValueError:
            print("Phone number must be an integer only!")
    return phone_number

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    # Display pizzas
    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(str(i+1) + '. ' + premium_pizzas[i])

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(str(i+1) + '. ' + gourmet_pizzas[i])

    # Pizza selection
    select_pizzas(num_pizzas)

def select_pizzas(num_pizzas):
    for _ in range(num_pizzas):
        selected = -1
        while selected < 1 or selected > len(premium_pizzas):
            try:
                selected = int(input('Select Your Premium Pizza (or 0 to skip): '))
                if selected > 0:
                    pizza_dict['num_premium_pizzas'] += 1
            except ValueError:
                print('Invalid Input')

    for _ in range(num_pizzas):
        selected = -1
        while selected < 1 or selected > len(gourmet_pizzas):
            try:
                selected = int(input('Select Your Gourmet Pizza (or 0 to skip): '))
                if selected > 0:
                    pizza_dict['num_gourmet_pizzas'] += 1
            except ValueError:
                print('Invalid Input')

def user_info():
    while True:
        choice = input("Press 1 for delivery or 2 for pickup: ")
        if choice == "1":
            delivery_details()
            return
        elif choice == "2":
            pizza_list()
            return
        else:
            print("Invalid choice, please try again.")

# Main flow
customer_name = customer_name()
phone_number = get_phone_number()
user_info()

# Output final information
print('\nTotal number of premium pizzas:', pizza_dict['num_premium_pizzas'])
print('Total number of gourmet pizzas:', pizza_dict['num_gourmet_pizzas'])

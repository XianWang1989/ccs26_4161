
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme",
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.isalpha():  # Ensure name is not a number
                return name
            else:
                print("Error: Name cannot be a number!")
        except ValueError:
            print("Error: You must enter something!")

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address:  # Ensure address is not empty
                return address
            else:
                print("Error: Address cannot be empty!")
        except ValueError:
            print("Error: You must enter something!")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number: "))
            if phone > 0:  # Ensure phone number is positive
                return phone
            else:
                print("Error: Phone number must be a positive integer!")
        except ValueError:
            print("Error: Phone number must be an integer!")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    pizza_dict = {
        "premium_pizza_price": 8.50,
        "gourmet_pizza_price": 5.00,
        "num_premium_pizzas": 0,
        "num_gourmet_pizzas": 0
    }

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    print('\nType "next" to move on.\n')

    for pizza_type in ['Premium', 'Gourmet']:
        while num_pizzas > 0:
            try:
                selected = input(f'Select Your {pizza_type} Pizza (or type "next"): ')
                if selected.lower() == 'next':
                    break
                else:
                    selected = int(selected)
                    if 1 <= selected <= (len(premium_pizzas) if pizza_type == 'Premium' else len(gourmet_pizzas)):
                        if pizza_type == 'Premium':
                            pizza_dict['num_premium_pizzas'] += 1
                        else:
                            pizza_dict['num_gourmet_pizzas'] += 1
                        num_pizzas -= 1
                    else:
                        print('Invalid Input')
            except ValueError:
                print('Invalid Input')

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number()
    pizza_list()

    print(f"\nCustomer Name: {name}\nDelivery Address: {address}\nPhone Number: {phone}")

# Start the program
main()


premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham" , "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name:
            return name
        else:
            print("Error: You must enter something!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        else:
            print("Error: You must enter something!")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number:\n"))
            if len(str(phone)) != 7:  # assuming a 7 digit requirement
                print("Phone number must be 7 digits.")
                continue
            return phone
        except ValueError:
            print("Phone number must be integer only (No letters allowed).")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    # More code for pizza selection can be added here...

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number()
    pizza_list()

    # Print collected details
    print(f"Name: {name}, Address: {address}, Phone: {phone}")

main()

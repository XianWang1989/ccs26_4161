
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name != "":
            return name
        print("Error: You must enter a valid name!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address != "":
            return address
        print("Error: You must enter a valid address!")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number (digits only): "))
            if phone_number > 0:
                return phone_number
        except ValueError:
            pass
        print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input. Please try again.')

    pizza_dict = {'num_premium_pizzas': 0, 'num_gourmet_pizzas': 0}

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    # Collecting selected pizzas
    while num_pizzas > 0:
        selected = input('Select Your Premium Pizza (or type "next" to move on): ')
        if selected == 'next':
            break
        try:
            selected = int(selected)
            if 1 <= selected <= len(premium_pizzas):
                pizza_dict['num_premium_pizzas'] += 1
                num_pizzas -= 1
                print("Selected Premium Pizza:", premium_pizzas[selected - 1])
            else:
                print('Invalid Input')
        except ValueError:
            print('Invalid Input')

    num_pizzas = int(input('How many gourmet pizzas would you like? '))

    while num_pizzas > 0:
        selected = input('Select Your Gourmet Pizza (or type "next" to move on): ')
        if selected == 'next':
            break
        try:
            selected = int(selected)
            if 1 <= selected <= len(gourmet_pizzas):
                pizza_dict['num_gourmet_pizzas'] += 1
                num_pizzas -= 1
                print("Selected Gourmet Pizza:", gourmet_pizzas[selected - 1])
            else:
                print('Invalid Input')
        except ValueError:
            print('Invalid Input')

    return pizza_dict

def main():
    name = customer_name()
    address = delivery_details()
    phone_number = get_phone_number()
    pizzas = pizza_list()

    # Compile receipt information
    receipt = {
        'Name': name,
        'Address': address,
        'Phone Number': phone_number,
        'Pizzas': pizzas
    }

    print("\nReceipt:")
    print(receipt)

if __name__ == "__main__":
    main()

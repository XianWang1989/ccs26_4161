
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham" , "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "selected_pizzas": 0,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0,
}

# Define all necessary functions first, followed by a main function to orchestrate the flow.
def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name.strip() != "":
            return name
        else:
            print("Error: You must enter a valid name.")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address.strip() != "":
            return address
        else:
            print("Error: You must enter a valid delivery address.")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number (digits only): "))
            if len(str(phone)) >= 7:  # Ensure phone number is at least 7 digits
                return phone
            else:
                print("Error: Phone number must be at least 7 digits.")
        except ValueError:
            print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while (num_pizzas <= 0) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input: Please enter a number.')

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(str(i + 1) + '. ' + premium_pizzas[i])
    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(str(i + 1) + '. ' + gourmet_pizzas[i])

    # Pizza selection
    select_pizzas(num_pizzas)

def select_pizzas(num_pizzas):
    # Selecting premium pizzas
    for _ in range(num_pizzas):
        while True:
            selected = input('Select Your Premium Pizza (or type "next" to skip): ')
            if selected == 'next':
                break
            try:
                selected = int(selected)
                if selected > 0 and selected <= len(premium_pizzas):
                    pizza_dict['num_premium_pizzas'] += 1
                    print(f"You selected: {premium_pizzas[selected - 1]}")
                    break
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

    # Selecting gourmet pizzas
    for _ in range(num_pizzas):
        while True:
            selected = input('Select Your Gourmet Pizza (or type "next" to skip): ')
            if selected == 'next':
                break
            try:
                selected = int(selected)
                if selected > 0 and selected <= len(gourmet_pizzas):
                    pizza_dict['num_gourmet_pizzas'] += 1
                    print(f"You selected: {gourmet_pizzas[selected - 1]}")
                    break
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

def main():
    name = customer_name()
    phone = phone_number()
    address = delivery_details()

    pizza_list()  # Call to the pizza selection function

    # At this point, you can print your receipt with the user's information.
    print(f"\nReceipt:\nName: {name}\nPhone: {phone}\nAddress: {address}")
    print(f'Total number of premium pizzas: {pizza_dict["num_premium_pizzas"]}')
    print(f'Total number of gourmet pizzas: {pizza_dict["num_gourmet_pizzas"]}')

if __name__ == "__main__":
    main()

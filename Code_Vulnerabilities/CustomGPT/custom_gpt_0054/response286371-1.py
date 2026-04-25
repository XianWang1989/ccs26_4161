
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def get_customer_name():
    while True:
        customer_name = input("Please enter your name: ")
        if customer_name:
            return customer_name
        else:
            print("Error: You must enter a name!")

def get_delivery_details():
    while True:
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address:
            return delivery_address
        else:
            print("Error: You must enter an address!")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number (numeric only): "))
            if len(str(phone_number)) >= 7:  # Ensure it's a valid number
                return phone_number
            else:
                print("Phone number must be at least 7 digits.")
        except ValueError:
            print("Error: Phone number must be an integer.")

def get_num_pizzas():
    while True:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if 1 <= num_pizzas <= 5:
                return num_pizzas
            else:
                print('Invalid Input: Choose a number between 1 and 5.')
        except ValueError:
            print('Invalid Input: Please enter a number.')

def pizza_selection(num_pizzas):
    selected_pizzas = []

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    for i in range(num_pizzas):
        while True:
            try:
                selected = int(input('Select Your Premium Pizza (Enter the number): '))
                if 1 <= selected <= len(premium_pizzas):
                    selected_pizzas.append(premium_pizzas[selected - 1])
                    break
                else:
                    print('Invalid Input: Please select a pizza from the list.')
            except ValueError:
                print('Invalid Input: Please enter a number.')

    print("You have selected the following pizzas: ", selected_pizzas)

def main():
    name = get_customer_name()
    address = get_delivery_details()
    phone = get_phone_number()
    num_pizzas = get_num_pizzas()

    pizza_selection(num_pizzas)

    # Now you can summarize the order or do something with the information collected
    print(f"\nCustomer Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {phone}")

if __name__ == "__main__":
    main()

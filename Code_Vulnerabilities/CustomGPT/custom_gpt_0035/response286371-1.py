
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme",
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ",
    "BBQ Chicken", "Hellfire"
]

def get_customer_name():
    while True:
        name = input("Please enter your name: ")
        if name.strip():
            return name
        print("Error: Name cannot be empty.")

def get_delivery_address():
    while True:
        address = input("Please enter your delivery address: ")
        if address.strip():
            return address
        print("Error: Address cannot be empty.")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if len(str(phone_number)) >= 7:  # check for a valid phone number length
                return phone_number
        except ValueError:
            print("Phone number must be an integer only (No letters).")
        print("Error: Phone number must be at least 7 digits.")

def get_num_pizzas():
    while True:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if 1 <= num_pizzas <= 5:
                return num_pizzas
        except ValueError:
            pass
        print('Invalid input. Please enter a number between 1 and 5.')

def select_pizzas(pizza_list, num_pizzas):
    selected_pizzas = []
    for i in range(num_pizzas):
        while True:
            try:
                selection = int(input(f'Select your pizza {i + 1} (1-{len(pizza_list)}): '))
                if 1 <= selection <= len(pizza_list):
                    selected_pizzas.append(pizza_list[selection - 1])
                    break
                else:
                    print('Invalid selection.')
            except ValueError:
                print('Invalid input, please enter a number.')
    return selected_pizzas

def main():
    customer_name = get_customer_name()
    phone_number = get_phone_number()
    delivery_address = get_delivery_address()

    num_pizzas = get_num_pizzas()

    print('\n==Premium Pizzas==')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f'{i}. {pizza}')

    premium_selection = select_pizzas(premium_pizzas, num_pizzas)

    print('\n==Gourmet Pizzas==')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f'{i}. {pizza}')

    gourmet_selection = select_pizzas(gourmet_pizzas, num_pizzas)

    # Final Output
    print("\nReceipt:")
    print(f'Customer Name: {customer_name}')
    print(f'Phone Number: {phone_number}')
    print(f'Delivery Address: {delivery_address}')
    print(f'Selected Premium Pizzas: {premium_selection}')
    print(f'Selected Gourmet Pizzas: {gourmet_selection}')

if __name__ == "__main__":
    main()

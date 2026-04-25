
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    name = ""
    while not name:
        name = input("Please enter your name: ")
        if not name.isalpha():
            print("Error: Name cannot be a number or empty.")
            name = ""
    return name

def delivery_details():
    address = ""
    while not address:
        address = input("Please enter your delivery address: ")
        if not address:
            print("Error: Address cannot be empty.")
    return address

def get_phone_number():
    phone_number = -1
    while phone_number < 0 or len(str(phone_number)) < 7:
        try:
            phone_number = int(input("Please enter your phone number (7 digits): "))
        except ValueError:
            print("Error: Phone number must be an integer.")
    return phone_number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (1-5): '))
        except ValueError:
            print('Invalid input.')

    pizzas_selected = []

    while num_pizzas > 0:
        print('\n==Premium Pizzas==\n')
        for i, pizza in enumerate(premium_pizzas, start=1):
            print(f"{i}. {pizza}")

        selected = input('Select Your Premium Pizza (or type "next" to skip): ')
        if selected.lower() == 'next':
            break
        else:
            try:
                selected = int(selected)
                if 1 <= selected <= len(premium_pizzas):
                    pizzas_selected.append(premium_pizzas[selected - 1])
                    num_pizzas -= 1
                else:
                    print('Invalid input')
            except ValueError:
                print('Invalid input')

    return pizzas_selected

def main():
    name = customer_name()
    address = delivery_details()
    phone_number = get_phone_number()
    selected_pizzas = pizza_list()

    print(f"\nCustomer Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {phone_number}")
    print(f"Selected Pizzas: {selected_pizzas}")

main()

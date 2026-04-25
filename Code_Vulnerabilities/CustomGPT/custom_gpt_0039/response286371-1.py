
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

# Initialize variables globally to store user data
customer_name_value = ""
delivery_address_value = ""
phone_number = ""
num_pizzas = -1


def customer_name():
    global customer_name_value
    while customer_name_value == "":
        try:
            customer_name_value = str(input("Please enter your name: "))
            if customer_name_value.isdigit():
                raise ValueError("Name cannot be a number.")
        except ValueError as e:
            print(e)

    user_info()


def delivery_details():
    global delivery_address_value
    while delivery_address_value == "":
        try:
            delivery_address_value = str(input("Please enter your delivery address: "))
        except:
            print("Error: You must enter something!")


def phone_input():
    global phone_number
    while not phone_number.isdigit() or len(phone_number) < 7:
        try:
            phone_number = input("Please enter your phone number (at least 7 digits): ")
            if not phone_number.isdigit():
                raise ValueError("Phone number must be digits only.")
        except ValueError as e:
            print(e)

    pizza_list()


def pizza_list():
    global num_pizzas
    while (num_pizzas <= 0) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    # Display pizzas
    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    # Select pizzas
    pizza_selection()


def pizza_selection():
    selected_premium = []
    selected_gourmet = []

    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input('Select Your Premium Pizza (or enter 0 to skip to Gourmet): '))
                if selected == 0:
                    break
                if selected <= 0 or selected > len(premium_pizzas):
                    print('Invalid Input')
                else:
                    selected_premium.append(premium_pizzas[selected - 1])
            except ValueError:
                print('Invalid Input')

    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input('Select Your Gourmet Pizza (or enter 0 to finish): '))
                if selected == 0:
                    break
                if selected <= 0 or selected > len(gourmet_pizzas):
                    print('Invalid Input')
                else:
                    selected_gourmet.append(gourmet_pizzas[selected - 1])
            except ValueError:
                print('Invalid Input')

    print_receipt(selected_premium, selected_gourmet)


def print_receipt(selected_premium, selected_gourmet):
    print(f"\nCustomer Name: {customer_name_value}")
    print(f"Delivery Address: {delivery_address_value}")
    print(f"Phone Number: {phone_number}")
    print(f"Selected Premium Pizzas: {selected_premium}")
    print(f"Selected Gourmet Pizzas: {selected_gourmet}")


def user_info():
    get_user_info = ""
    while not get_user_info in ["1", "2"]:
        get_user_info = str(input("Press 1 for delivery, Press 2 for pickup: "))
    if get_user_info == "1":
        delivery_details()
        phone_input()
    elif get_user_info == "2":
        pizza_list()


# Start the process
customer_name()

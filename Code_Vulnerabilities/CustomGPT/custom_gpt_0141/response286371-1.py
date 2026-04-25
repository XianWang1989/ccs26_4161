
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    name = ""
    while name == "":
        try:
            name = input("Please enter your name: ")
            if not name.isalpha():  # Ensure name is not a number
                raise ValueError("Name cannot be a number.")
        except ValueError as e:
            print(e)

    return name

def phone_number():
    phone = ""
    while True:
        try:
            phone = input("Please enter your phone number: ")
            if len(phone) < 7 or not phone.isdigit():
                raise ValueError("Phone number must be at least 7 digits.")
            break  # Valid phone number, exit loop
        except ValueError as e:
            print(e)

    return phone

def delivery_details():
    address = ""
    while address == "":
        try:
            address = input("Please enter your delivery address: ")
            if not address:
                raise ValueError("Address cannot be empty.")
        except ValueError as e:
            print(e)

    return address

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:  # Ensure the number of pizzas is valid
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if num_pizzas < 1 or num_pizzas > 5:
                raise ValueError("Choose between 1 and 5 pizzas.")
        except ValueError as e:
            print(e)

    selected_pizzas = []
    print('\n== Premium Pizzas ==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n== Gourmet Pizzas ==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input('Select your Premium Pizza (enter number): '))
                if selected < 1 or selected > len(premium_pizzas):
                    raise ValueError("Invalid input.")
                selected_pizzas.append(premium_pizzas[selected - 1])
                break
            except ValueError as e:
                print(e)

    return selected_pizzas

def summary(customer_name, phone, address, pizzas):
    print('\n--- Order Summary ---')
    print(f'Customer Name: {customer_name}')
    print(f'Phone Number: {phone}')
    print(f'Delivery Address: {address}')
    print('Pizzas Ordered:')
    for pizza in pizzas:
        print(f'- {pizza}')

# Main program flow
def main():
    name = customer_name()
    phone = phone_number()
    address = delivery_details()
    pizzas = pizza_list()
    summary(name, phone, address, pizzas)

if __name__ == "__main__":
    main()

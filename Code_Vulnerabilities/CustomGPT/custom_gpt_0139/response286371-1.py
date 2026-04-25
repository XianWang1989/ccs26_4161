
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        try:
            name = str(input("Please enter your name: "))
            if name:
                return name
        except:
            print("Error! You must enter your name.")

def delivery_details():
    while True:
        try:
            address = str(input("Please enter your delivery address: "))
            if address:
                return address
        except:
            print("Error! You must enter a delivery address.")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if phone_number > 0:  # Ensure it's a positive number
                return phone_number
        except ValueError:
            print("Phone number must be an integer only.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    selected_pizzas = []

    # Premium Pizzas selection
    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(str(i + 1) + '. ' + premium_pizzas[i])

    for _ in range(num_pizzas):
        selected = int(input('Select Your Premium Pizza (enter number): '))
        selected_pizzas.append(premium_pizzas[selected - 1])

    return selected_pizzas

def main():
    name = customer_name()
    address = delivery_details()
    phone_number = get_phone_number()
    selected_pizzas = pizza_list()

    print("\nReceipt:")
    print(f"Customer Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {phone_number}")
    print(f"Selected Pizzas: {selected_pizzas}")

if __name__ == "__main__":
    main()


premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name.strip():
            return name
        print("Error: You must enter a valid name!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address.strip():
            return address
        print("Error: You must enter a valid address!")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if phone_number > 0:  # Validate phone number
                return phone_number
            else:
                print("Phone number must be a positive integer.")
        except ValueError:
            print("Phone number must be an integer only.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input.')

    # Display pizza options
    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, 1):
        print(f"{i}. {pizza}")
    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, 1):
        print(f"{i}. {pizza}")

    selected_pizzas = []
    for _ in range(num_pizzas):
        while True:
            selected = input('Select your pizza (or type "next" to finish): ')
            if selected.lower() == "next":
                break
            try:
                selected = int(selected)
                if 1 <= selected <= len(premium_pizzas) + len(gourmet_pizzas):
                    selected_pizzas.append(selected)
                    break
                else:
                    print("Invalid choice, please try again.")
            except ValueError:
                print("Invalid input, please try again.")

    return selected_pizzas

def user_info():
    while True:
        choice = input("Press 1 for delivery or 2 for pickup: ")
        if choice == "1":
            delivery_details()
            return
        elif choice == "2":
            return
        else:
            print("Invalid choice, please try again.")

def main():
    name = customer_name()
    phone_number = get_phone_number()
    pizzas = pizza_list()
    user_info()

    # Print details
    print(f"\nCustomer Name: {name}")
    print(f"Phone Number: {phone_number}")
    print(f"Selected Pizzas: {pizzas}")

if __name__ == "__main__":
    main()

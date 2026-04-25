
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if not name.isdigit() and name:  # Check if input is not a number and is not empty
                return name
            else:
                print("Error: Name must not be a number and cannot be empty.")
        except ValueError:
            print("Error: Invalid input.")

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address:  # Ensure the address is not empty
                return address
            else:
                print("Error: Address cannot be empty.")
        except ValueError:
            print("Error: Invalid input.")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number (digits only): "))
            if 1000000 <= phone_number <= 9999999:  # Assuming 7-digit phone number
                return phone_number
            else:
                print("Error: Phone number must be a valid 7-digit number.")
        except ValueError:
            print("Error: Phone number must be integer only.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input("How many pizzas would you like (max of 5): "))
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and 5.")

    pizza_dict = {
        "premium_pizza_price": 8.50,
        "gourmet_pizza_price": 5.00,
        "num_premium_pizzas": 0,
        "num_gourmet_pizzas": 0
    }

    print('\n==Premium Pizzas==')
    for i, pizza in enumerate(premium_pizzas, 1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==')
    for i, pizza in enumerate(gourmet_pizzas, 1):
        print(f"{i}. {pizza}")

    selected_premium = []
    selected_gourmet = []

    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input("Select Your Premium Pizza (or enter 0 to skip): "))
                if selected == 0:
                    break
                elif 1 <= selected <= len(premium_pizzas):
                    selected_premium.append(premium_pizzas[selected - 1])
                    pizza_dict['num_premium_pizzas'] += 1
                    break
                else:
                    print("Invalid Input")
            except ValueError:
                print("Invalid Input")

    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input("Select Your Gourmet Pizza (or enter 0 to skip): "))
                if selected == 0:
                    break
                elif 1 <= selected <= len(gourmet_pizzas):
                    selected_gourmet.append(gourmet_pizzas[selected - 1])
                    pizza_dict['num_gourmet_pizzas'] += 1
                    break
                else:
                    print("Invalid Input")
            except ValueError:
                print("Invalid Input")

    return selected_premium, selected_gourmet, pizza_dict

def main():
    name = customer_name()
    address = delivery_details()
    phone_number = get_phone_number()
    selected_premium, selected_gourmet, pizza_dict = pizza_list()

    # Print summary
    print(f"\nCustomer Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {phone_number}")
    print(f"Selected Premium Pizzas: {selected_premium}")
    print(f"Selected Gourmet Pizzas: {selected_gourmet}")
    print(f"Total Premium Pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Total Gourmet Pizzas: {pizza_dict['num_gourmet_pizzas']}")

if __name__ == "__main__":
    main()

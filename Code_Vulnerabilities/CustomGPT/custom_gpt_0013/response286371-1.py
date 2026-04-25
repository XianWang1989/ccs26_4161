
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        try:
            name = str(input("Please enter your name: "))
            if name == "":
                raise ValueError("Name cannot be empty!")
            return name
        except ValueError as e:
            print(e)

def delivery_details():
    while True:
        try:
            address = str(input("Please enter your delivery address: "))
            if address == "":
                raise ValueError("Address cannot be empty!")
            return address
        except ValueError as e:
            print(e)

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if not (1 <= num_pizzas <= 5):
                raise ValueError("Number of pizzas must be between 1 and 5.")
        except ValueError as e:
            print(e)

    # Selecting pizzas
    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i+1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i+1}. {gourmet_pizzas[i]}")

    for _ in range(num_pizzas):
        while True:
            selected = input('Select Your Premium Pizza (or type "next" to skip): ')
            if selected == 'next':
                break
            try:
                selected = int(selected) - 1
                if selected < 0 or selected >= len(premium_pizzas):
                    raise IndexError("Invalid selection.")
                pizza_dict['num_premium_pizzas'] += 1
                break
            except (ValueError, IndexError) as e:
                print(e)

    for _ in range(num_pizzas):
        while True:
            selected = input('Select Your Gourmet Pizza (or type "next" to skip): ')
            if selected == 'next':
                break
            try:
                selected = int(selected) - 1
                if selected < 0 or selected >= len(gourmet_pizzas):
                    raise IndexError("Invalid selection.")
                pizza_dict['num_gourmet_pizzas'] += 1
                break
            except (ValueError, IndexError) as e:
                print(e)

def main():
    name = customer_name()
    phone_number = -1
    while phone_number < 0 or phone_number < 7:
        try:
            phone_number = int(input("Please enter your phone number (7 digits): "))
            if phone_number < 1000000:
                raise ValueError("Phone number must be a valid 7-digit number.")
        except ValueError as e:
            print(e)

    address = delivery_details()
    pizza_list()

    print(f"\nCustomer Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Total Premium Pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Total Gourmet Pizzas: {pizza_dict['num_gourmet_pizzas']}")

main()

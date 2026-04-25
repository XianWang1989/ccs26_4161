
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme",
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ")
    return name

def delivery_details():
    address = ""
    while address == "":
        address = input("Please enter your delivery address: ")
    return address

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if phone_number > 0 and len(str(phone_number)) >= 7:  # Ensure valid length
                return phone_number
            else:
                print("Phone number must be at least 7 digits.")
        except ValueError:
            print("Phone number must be an integer.")

def pizza_list():
    num_pizzas = 0
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f'{i}. {pizza}')

    # Select premium pizzas
    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input('Select Your Premium Pizza (or enter 0 to skip): '))
                if selected == 0:
                    break
                if 1 <= selected <= len(premium_pizzas):
                    pizza_dict['num_premium_pizzas'] += 1
                    break
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

    # Select gourmet pizzas similar to above...

def main():
    name = customer_name()
    phone_number = get_phone_number()
    delivery_address = delivery_details()
    pizza_list()

    # Print receipt
    print(f"Customer Name: {name}")
    print(f"Phone Number: {phone_number}")
    print(f"Delivery Address: {delivery_address}")
    print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
    # Add gourmet pizzas total calculation if needed

main()

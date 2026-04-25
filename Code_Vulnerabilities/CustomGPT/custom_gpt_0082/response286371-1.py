
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

def get_customer_name():
    while True:
        customer_name = input("Please enter your name: ")
        if customer_name.isalpha():
            return customer_name
        else:
            print("Error: Name must contain only letters.")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if phone_number >= 1000000:  # basic check for length
                return phone_number
            else:
                print("Phone number must be at least 7 digits.")
        except ValueError:
            print("Phone number must be an integer.")

def get_delivery_details():
    delivery_address = input("Please enter your delivery address: ")
    return delivery_address

def get_number_of_pizzas():
    while True:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5):'))
            if 0 < num_pizzas <= 5:
                return num_pizzas
            else:
                print('Invalid Input. Must be between 1 and 5.')
        except ValueError:
            print('Invalid Input. Please enter a number.')

def pizza_selection(pizza_list, max_pizzas):
    num_pizzas = max_pizzas
    selected_pizzas = []

    while num_pizzas > 0:
        print(f'You can select {num_pizzas} more pizzas.')
        print("Available pizzas:")
        for i, pizza in enumerate(pizza_list, 1):
            print(f"{i}. {pizza}")

        try:
            selected = int(input('Select a pizza by number (or enter 0 to move on): '))
            if selected == 0:
                break
            elif 1 <= selected <= len(pizza_list):
                selected_pizzas.append(pizza_list[selected - 1])
                num_pizzas -= 1
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    return selected_pizzas

def main():
    customer_name = get_customer_name()
    phone_number = get_phone_number()
    delivery_address = get_delivery_details()

    num_pizzas = get_number_of_pizzas()
    premium_selections = pizza_selection(premium_pizzas, num_pizzas)
    gourmet_selections = pizza_selection(gourmet_pizzas, num_pizzas)

    print("\nOrder Summary:")
    print(f"Customer Name: {customer_name}")
    print(f"Phone Number: {phone_number}")
    print(f"Delivery Address: {delivery_address}")
    print("Premium Pizzas Selected:", premium_selections)
    print("Gourmet Pizzas Selected:", gourmet_selections)

main()

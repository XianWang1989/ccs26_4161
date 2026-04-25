
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
                  "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
                  "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "selected_pizzas": 0,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        customer_name = input("Please enter your name: ")
        if customer_name.strip():
            return customer_name
        else:
            print("Error: You must enter a name!")

def delivery_details():
    while True:
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address.strip():
            return delivery_address
        else:
            print("Error: You must enter an address!")

def phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number: "))
            if phone_number > 0:
                return phone_number
        except ValueError:
            print("Phone number must be an integer only.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 5.')

    for i, pizza in enumerate(premium_pizzas):
        print(f"{i + 1}. {pizza}")

    for i, pizza in enumerate(gourmet_pizzas):
        print(f"{i + 1}. {pizza}")

    selected_pizzas = []
    while num_pizzas > 0:
        selected = input('Select a Premium Pizza (or type "next" to move on): ')
        if selected.lower() == 'next':
            break
        else:
            try:
                selected = int(selected)
                if 1 <= selected <= len(premium_pizzas):
                    selected_pizzas.append(premium_pizzas[selected - 1])
                    num_pizzas -= 1
                else:
                    print('Invalid input.')
            except ValueError:
                print('Invalid input.')

    return selected_pizzas

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number()
    pizzas = pizza_list()

    print(f"\nReceipt for {name}:")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {phone}")
    print("Selected Pizzas:", ", ".join(pizzas))

if __name__ == "__main__":
    main()

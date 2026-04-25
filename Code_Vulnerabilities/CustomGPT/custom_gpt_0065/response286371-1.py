
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
                  "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", 
                  "Vegetriano"]
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
        name = input("Please enter your name: ")
        if name != "":
            return name
        print("Error: you must enter a name!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address != "":
            return address
        print("Error: you must enter an address!")

def phone_number():
    while True:
        try:
            number = int(input("Please enter your phone number: "))
            if number >= 1000000:  # Example condition for valid phone number
                return number
        except ValueError:
            print("Error: Phone number must be an integer only.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f'{i}. {pizza}')

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f'{i}. {pizza}')

    selected_pizzas = []
    while num_pizzas > 0:
        selected = input('Select your pizza (type "next" to skip): ')
        if selected.lower() == 'next':
            break
        try:
            selected = int(selected)
            if 1 <= selected <= len(premium_pizzas):
                selected_pizzas.append(premium_pizzas[selected - 1])
                num_pizzas -= 1
            else:
                print('Invalid selection')
        except ValueError:
            print('Invalid input')

    return selected_pizzas

def main():
    name = customer_name()
    address = delivery_details()
    number = phone_number()
    selected_pizzas = pizza_list()

    print(f"\nReceipt for {name}:")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {number}")
    print(f"Selected Pizzas: {', '.join(selected_pizzas)}")

if __name__ == "__main__":
    main()

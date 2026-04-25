
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.isdigit() or name == "":
                raise ValueError("Name cannot be a number or empty!")
            return name
        except ValueError as e:
            print(e)

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address == "":
                raise ValueError("Address cannot be empty!")
            return address
        except ValueError as e:
            print(e)

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number (digits only): "))
            if len(str(phone)) < 7:
                raise ValueError("Phone number must be at least 7 digits.")
            return phone
        except ValueError as e:
            print(e)

def pizza_list():
    num_pizzas = -1
    pizza_dict = {
        "premium_pizza_price": 8.50,
        "gourmet_pizza_price": 5.00,
        "num_premium_pizzas": 0,
        "num_gourmet_pizzas": 0
    }

    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    while num_pizzas > 0:
        try:
            selected = int(input('Select Your Premium Pizza: '))
            if 1 <= selected <= len(premium_pizzas):
                pizza_dict['num_premium_pizzas'] += 1
                num_pizzas -= 1
            else:
                print('Invalid Input')
        except ValueError:
            print('Invalid Input')

    return pizza_dict

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number()
    pizza_dict = pizza_list()

    print(f"\nCustomer Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {phone}")
    print(f"Total Premium Pizzas Ordered: {pizza_dict['num_premium_pizzas']}")
    total_cost = pizza_dict["num_premium_pizzas"] * pizza_dict['premium_pizza_price']
    print(f"Total Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()

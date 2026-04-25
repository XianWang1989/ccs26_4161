
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.isalpha():
                return name
            else:
                print("Error: Name must not contain numbers.")
        except Exception as e:
            print("Error: Something went wrong.")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        else:
            print("Error: Address cannot be empty.")

def phone_number():
    while True:
        try:
            number = int(input("Please enter your phone number (digits only): "))
            if number > 0:
                return number
            else:
                print("Error: Phone number must be a positive integer.")
        except ValueError:
            print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    pizza_dict = {"num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    print('\n==Premium Pizzas==\n')
    for idx, pizza in enumerate(premium_pizzas, start=1):
        print(f"{idx}. {pizza}")

    for _ in range(num_pizzas):
        selected = int(input('Select Your Premium Pizza by number: '))
        if 1 <= selected <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1
        else:
            print('Invalid Input')

    print('\n==Gourmet Pizzas==\n')
    for idx, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{idx}. {pizza}")

    for _ in range(num_pizzas):
        selected = int(input('Select Your Gourmet Pizza by number: '))
        if 1 <= selected <= len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1
        else:
            print('Invalid Input')

    return pizza_dict

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number()
    pizza_order = pizza_list()

    receipt = {
        "name": name,
        "address": address,
        "phone": phone,
        "pizzas": pizza_order
    }

    print("\nReceipt:")
    print(receipt)

if __name__ == "__main__":
    main()

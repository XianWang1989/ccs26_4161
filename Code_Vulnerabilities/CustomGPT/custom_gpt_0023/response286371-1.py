
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ").strip()
        if name == "":
            print("Error: You must enter a name!")
    return name

def delivery_details():
    address = ""
    while address == "":
        address = input("Please enter your delivery address: ").strip()
        if address == "":
            print("Error: You must enter an address!")
    return address

def phone_number_input():
    phone_number = -1
    while phone_number <= 0 or len(str(phone_number)) < 7:
        try:
            phone_number = int(input("Please enter your phone number (at least 7 digits): "))
            if phone_number <= 0 or len(str(phone_number)) < 7:
                print("Phone number must be at least 7 digits.")
        except ValueError:
            print("Phone number must be an integer.")
    return phone_number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if num_pizzas < 1 or num_pizzas > 5:
                print('Invalid Input: Please select a number between 1 and 5.')
        except ValueError:
            print('Invalid Input: Please enter an integer.')

    # Display pizzas
    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    # Select Premium Pizzas
    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input('Select Your Premium Pizza (1 to {} or enter 0 to skip): '.format(len(premium_pizzas))))
                if 0 <= selected <= len(premium_pizzas):
                    if selected > 0:
                        pizza_dict['num_premium_pizzas'] += 1
                    break
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

def collect_user_info():
    name = customer_name()
    phone = phone_number_input()
    address = delivery_details()
    return name, phone, address

def main():
    name, phone, address = collect_user_info()
    pizza_list()
    print(f"Name: {name}, Phone: {phone}, Address: {address}")
    print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")

if __name__ == "__main__":
    main()

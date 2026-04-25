
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

# Store user information
user_info_list = []

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name:
            user_info_list.append(name)
            break
        else:
            print("Error: you must enter a valid name!")


def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            user_info_list.append(address)
            break
        else:
            print("Error: you must enter a valid address!")


def phone_number_input():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if 1000000 <= phone_number <= 9999999:  # Example condition for 7-digit phone numbers
                user_info_list.append(phone_number)
                break
            else:
                print("Error: Phone number must be 7 digits.")
        except ValueError:
            print("Error: Phone number must be an integer.")


def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 5.')

    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i + len(premium_pizzas)}. {pizza}")

    for _ in range(num_pizzas):
        selected = int(input("Select your pizza (by number): "))
        if 1 <= selected <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1
        elif len(premium_pizzas) + 1 <= selected <= len(premium_pizzas) + len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1
        else:
            print("Invalid selection.")

def main():
    customer_name()
    phone_number_input()
    delivery_details()
    pizza_list()

    print("\nUser Information:")
    for info in user_info_list:
        print(info)

    total_cost = (pizza_dict['num_premium_pizzas'] * pizza_dict['premium_pizza_price'] +
                  pizza_dict['num_gourmet_pizzas'] * pizza_dict['gourmet_pizza_price'])
    print(f'\nTotal cost: {total_cost:.2f}')

if __name__ == "__main__":
    main()

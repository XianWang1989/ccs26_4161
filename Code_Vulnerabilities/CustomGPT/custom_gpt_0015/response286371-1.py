
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme",
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ",
    "BBQ Chicken", "Hellfire"
]

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.isalpha():  # Ensure it's a valid name
                return name
            else:
                print("Error: Name cannot contain numbers or special characters!")
        except Exception as e:
            print(f"Error: {e}")

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address:  # Ensure it's not empty
                return address
            else:
                print("Error: Address must not be empty!")
        except Exception as e:
            print(f"Error: {e}")

def phone_number():
    while True:
        try:
            number = int(input("Please enter your phone number:\n\t"))
            if len(str(number)) >= 7:  # Ensure it's at least 7 digits
                return number
            else:
                print("Error: Phone number must be at least 7 digits long!")
        except ValueError:
            print("Phone number must be an integer only.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    pizza_dict = {
        "premium_pizza_price": 8.50,
        "gourmet_pizza_price": 5.00,
        "num_premium_pizzas": 0,
        "num_gourmet_pizzas": 0
    }

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    selected_pizzas(pizza_dict, num_pizzas, premium_pizzas, 'premium')
    selected_pizzas(pizza_dict, num_pizzas, gourmet_pizzas, 'gourmet')

    return pizza_dict

def selected_pizzas(pizza_dict, num_pizzas, pizza_list, pizza_type):
    for _ in range(num_pizzas):
        while True:
            try:
                selected = input(f'Select Your {pizza_type.capitalize()} Pizza (or type "next" to skip): ')
                if selected == 'next':
                    break
                selected = int(selected)
                if selected < 1 or selected > len(pizza_list):
                    print('Invalid Input')
                else:
                    pizza_dict[f'num_{pizza_type}_pizzas'] += 1
                    print(f"You selected: {pizza_list[selected - 1]}")
                    break
            except ValueError:
                print('Invalid Input')

def main():
    name = customer_name()
    number = phone_number()
    address = delivery_details()
    pizza_dict = pizza_list()

    receipt = {
        "name": name,
        "phone": number,
        "address": address,
        "num_premium_pizzas": pizza_dict['num_premium_pizzas'],
        "num_gourmet_pizzas": pizza_dict['num_gourmet_pizzas'],
    }

    print("\nReceipt:")
    print(receipt)

if __name__ == "__main__":
    main()

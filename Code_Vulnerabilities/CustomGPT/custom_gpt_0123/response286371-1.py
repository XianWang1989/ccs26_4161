
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

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

def phone_number():
    number = -1
    while number < 0 or number < 7:
        try:
            number = int(input("Please enter your phone number (digits only): "))
        except ValueError:
            print("Phone number must be an integer.")
    return number

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}
    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i+1}. {premium_pizzas[i]}")
    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i+1}. {gourmet_pizzas[i]}")

    while True:
        if num_pizzas == 0:
            break
        selected = input('Select Your Premium Pizza (or type "next" to continue): ')
        if selected == 'next':
            break
        try:
            selected = int(selected) - 1
            if selected < 0 or selected >= len(premium_pizzas):
                print('Invalid Input')
            else:
                pizza_dict['num_premium_pizzas'] += 1
                num_pizzas -= 1
        except ValueError:
            print('Invalid Input')

    while True:
        if num_pizzas == 0:
            break
        selected = input('Select Your Gourmet Pizza (or type "next" to continue): ')
        if selected == 'next':
            break
        try:
            selected = int(selected) - 1
            if selected < 0 or selected >= len(gourmet_pizzas):
                print('Invalid Input')
            else:
                pizza_dict['num_gourmet_pizzas'] += 1
                num_pizzas -= 1
        except ValueError:
            print('Invalid Input')

    return pizza_dict

def main():
    name = customer_name()
    address = delivery_details()
    number = phone_number()
    pizzas = pizza_list()

    # Collecting user details into a list
    user_details = [name, address, number, pizzas['num_premium_pizzas'], pizzas['num_gourmet_pizzas']]
    print("\nUser Details:", user_details)

if __name__ == "__main__":
    main()

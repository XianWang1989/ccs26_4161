
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    name = ""
    while name == "":
        try:
            name = input("Please enter your name: ")
        except ValueError:
            print("Error: You must enter a valid name!")
    return name

def delivery_details():
    address = ""
    while address == "":
        try:
            address = input("Please enter your delivery address: ")
        except ValueError:
            print("Error: You must enter a valid address!")
    return address

def phone_number():
    number = -1
    while number < 0 or len(str(number)) < 7:
        try:
            number = int(input("Please enter your phone number (at least 7 digits): "))
        except ValueError:
            print("Phone number must be an integer!")
    return number

def pizza_list():
    num_pizzas = -1
    pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input!')

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    selected_pizzas = []

    for _ in range(num_pizzas):
        selected = int(input('Select your pizza (1 for Premium, 2 for Gourmet, 0 to finish): '))
        if selected == 0:
            break
        elif selected <= len(premium_pizzas):
            pizza_dict['num_premium_pizzas'] += 1
            selected_pizzas.append(premium_pizzas[selected - 1])
        elif selected <= len(gourmet_pizzas):
            pizza_dict['num_gourmet_pizzas'] += 1
            selected_pizzas.append(gourmet_pizzas[selected - len(premium_pizzas) - 1])
        else:
            print('Invalid selection!')

    return pizza_dict, selected_pizzas

def main():
    name = customer_name()
    address = delivery_details()
    number = phone_number()
    pizza_dict, selected_pizzas = pizza_list()

    print(f"\nCustomer Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {number}")
    print(f"Selected Premium Pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Selected Gourmet Pizzas: {pizza_dict['num_gourmet_pizzas']}")
    print("Pizzas ordered:", selected_pizzas)

if __name__ == "__main__":
    main()

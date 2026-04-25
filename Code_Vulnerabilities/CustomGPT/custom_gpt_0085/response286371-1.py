
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    name = ""
    while name == "":
        try:
            name = input("Please enter your name: ")
            if name.isdigit():
                raise ValueError("Name cannot be a number.")
        except ValueError as e:
            print(e)
    return name

def delivery_details():
    address = ""
    while address == "":
        address = input("Please enter your delivery address: ")
    return address

def phone_number():
    phone = ""
    while True:
        try:
            phone = int(input("Please enter your phone number:\n\t"))
            if not (1000000 <= phone <= 9999999):  # Example check for a 7-digit number
                raise ValueError("Phone number must be 7 digits.")
            break
        except ValueError as e:
            print(e)
    return phone

def pizza_list():
    num_pizzas = -1
    while (num_pizzas < 0) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    pizza_dict = {"num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas):
        print(f"{i + 1}. {pizza}")

    while True:
        if num_pizzas <= 0:
            break
        try:
            selected = input('Select Your Premium Pizza (or type "next" to proceed): ')
            if selected.lower() == 'next':
                break
            selected = int(selected)
            if selected < 1 or selected > len(premium_pizzas):
                print('Invalid Input')
            else:
                pizza_dict['num_premium_pizzas'] += 1
                num_pizzas -= 1
        except ValueError:
            print('Invalid Input')

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas):
        print(f"{i + 1}. {pizza}")

    while True:
        if num_pizzas <= 0:
            break
        try:
            selected = input('Select Your Gourmet Pizza (or type "next" to proceed): ')
            if selected.lower() == 'next':
                break
            selected = int(selected)
            if selected < 1 or selected > len(gourmet_pizzas):
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
    phone = phone_number()
    pizzas = pizza_list()

    receipt = {
        "Name": name,
        "Address": address,
        "Phone": phone,
        "Pizzas": pizzas
    }

    print("\nReceipt:")
    print(receipt)

if __name__ == "__main__":
    main()

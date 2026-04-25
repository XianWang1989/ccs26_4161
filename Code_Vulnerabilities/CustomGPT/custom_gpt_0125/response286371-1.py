
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    customer_name = ""
    while customer_name == "":
        try:
            customer_name = str(input("Please enter your name: "))
        except:
            print("Error: You must enter something! (cannot be a number)")
    return customer_name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = str(input("Please enter your delivery address: "))
        except:
            print("Error: You must enter something!")
    return delivery_address

def get_phone_number():
    phone_number = ""
    while len(phone_number) < 7:
        try:
            phone_number = str(input("Please enter your phone number:\n\t"))
            if not phone_number.isdigit() or len(phone_number) < 7:
                raise ValueError
        except ValueError:
            print("Phone number must be at least 7 digits long.")
    return phone_number

def pizza_list():
    num_pizzas = -1
    while (num_pizzas < 0) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except:
            print('Invalid Input')

    pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00,
                  "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    while True:
        if num_pizzas == 0:
            break
        selected = input('Select Your Premium Pizza (or type "next" to proceed): ')
        if selected == 'next':
            break
        else:
            try:
                selected = int(selected)
                if 1 <= selected <= len(premium_pizzas):
                    pizza_dict['num_premium_pizzas'] += 1
                    num_pizzas -= 1
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

    while True:
        if num_pizzas == 0:
            break
        selected = input('Select Your Gourmet Pizza (or type "next" to proceed): ')
        if selected == 'next':
            break
        else:
            try:
                selected = int(selected)
                if 1 <= selected <= len(gourmet_pizzas):
                    pizza_dict['num_gourmet_pizzas'] += 1
                    num_pizzas -= 1
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

    return pizza_dict

def main():
    name = customer_name()
    phone = get_phone_number()
    address = delivery_details()
    pizzas = pizza_list()

    # Printing all details at the end
    print(f"\nCustomer Name: {name}")
    print(f"Phone Number: {phone}")
    print(f"Delivery Address: {address}")
    print(f"Total number of premium pizzas: {pizzas['num_premium_pizzas']}")
    print(f"Total number of gourmet pizzas: {pizzas['num_gourmet_pizzas']}")

main()


premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.strip() == "":
                raise ValueError("Name cannot be empty.")
            break
        except ValueError as e:
            print(e)
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = input("Please enter your delivery address: ")
            if delivery_address.strip() == "":
                raise ValueError("Address cannot be empty.")
        except ValueError as e:
            print(e)
    return delivery_address

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number (digits only): "))
            if phone < 1000000:  # Ensure a valid phone number
                raise ValueError("Phone number must be at least 7 digits.")
            return phone
        except ValueError as e:
            print(e)

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if num_pizzas < 1 or num_pizzas > 5:
                raise ValueError("Please select a number between 1 and 5.")
        except ValueError as e:
            print(e)

    selected_pizzas = []
    print('\n== Premium Pizzas ==')
    for idx, pizza in enumerate(premium_pizzas, start=1):
        print(f"{idx}. {pizza}")

    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input('Select Your Premium Pizza (1 to {}): '.format(len(premium_pizzas))))
                if selected < 1 or selected > len(premium_pizzas):
                    raise ValueError("Invalid selection. Please select a valid pizza.")
                selected_pizzas.append(premium_pizzas[selected - 1]) 
                break
            except ValueError as e:
                print(e)

    print("You selected the following pizzas: ", selected_pizzas)

def main():
    name = customer_name()
    address = delivery_details()
    phone = phone_number()
    pizza_list()

    print(f"Customer Name: {name}, Delivery Address: {address}, Phone Number: {phone}")

if __name__ == "__main__":
    main()


premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
                  "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", 
                  "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
                  "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name.isalpha():
            return name
        else:
            print("Error: Name cannot be a number!")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        else:
            print("Error: Address cannot be empty!")

def phone_number():
    while True:
        try:
            num = int(input("Please enter your phone number (digits only): "))
            if len(str(num)) >= 7:
                return num
            else:
                print("Error: Phone number must be at least 7 digits.")
        except ValueError:
            print("Error: Phone number must be a number.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    selected_pizzas = []

    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input('Select Your Premium Pizza (or enter 0 to skip): '))
                if selected == 0:
                    break
                if 1 <= selected <= len(premium_pizzas):
                    selected_pizzas.append(premium_pizzas[selected - 1])
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

    return selected_pizzas

def user_info():
    print("1. Delivery")
    print("2. Pickup")
    choice = input("Press 1 for delivery or 2 for pickup: ")

    if choice == "1":
        delivery_address = delivery_details()
        return ("Delivery", delivery_address)
    elif choice == "2":
        return ("Pickup", None)
    else:
        print("Invalid choice.")
        return user_info()  # Recursive call for valid choice

# Main execution
receipt = []
name = customer_name()
receipt.append(name)

phone = phone_number()
receipt.append(phone)

pizzas = pizza_list()
receipt.extend(pizzas)

info_type, address = user_info()
receipt.append((info_type, address))

print("\nReceipt:")
for item in receipt:
    print(item)

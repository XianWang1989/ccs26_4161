
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        name = input("Please enter your name: ")
        if name.isalpha():
            return name
        else:
            print("Error: You must enter a valid name (no numbers).")

def delivery_details():
    while True:
        address = input("Please enter your delivery address: ")
        if address:
            return address
        else:
            print("Error: You must enter something!")

def phone_number():
    while True:
        try:
            phone = int(input("Please enter your phone number (7 digits): "))
            if 1000000 <= phone < 10000000:  # Example validation for 7-digit numbers
                return phone
            else:
                print("Phone number must be 7 digits.")
        except ValueError:
            print("Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    selected_pizzas = []

    for _ in range(num_pizzas):
        while True:
            try:
                selected = int(input('Select Your Premium Pizza (or 0 to skip): '))
                if selected == 0:
                    break
                elif 1 <= selected <= len(premium_pizzas):
                    selected_pizzas.append(premium_pizzas[selected - 1])
                    pizza_dict['num_premium_pizzas'] += 1
                    break
                else:
                    print('Invalid Input')
            except ValueError:
                print('Invalid Input')

    return selected_pizzas

def user_info():
    choice = input("Press 1 for delivery, 2 for pickup: ")
    if choice == "1":
        delivery_details()
    elif choice == "2":
        pizza_list()
    else:
        print("Invalid option.")

# Main Program Logic
name = customer_name()
phone = phone_number()
user_info()  # This will handle gathering delivery or pickup info

# Print summary receipt
print(f"\nCustomer Name: {name}\nPhone Number: {phone}")
print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")

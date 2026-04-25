
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ")
        if name.isdigit():
            print("Error: Name cannot be a number!")
            name = ""
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        delivery_address = input("Please enter your delivery address: ")
    return delivery_address

def phone_number():
    phone = ""
    while len(phone) < 7 or not phone.isdigit():
        phone = input("Please enter your phone number (at least 7 digits): ")
    return phone

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
        print(f"{len(premium_pizzas) + i + 1}. {gourmet_pizzas[i]}")

    for _ in range(num_pizzas):
        selected = input('Select Your Pizza (enter the number): ')
        if selected.isdigit() and 1 <= int(selected) <= (len(premium_pizzas) + len(gourmet_pizzas)):
            if int(selected) <= len(premium_pizzas):
                pizza_dict['num_premium_pizzas'] += 1
            else:
                pizza_dict['num_gourmet_pizzas'] += 1
        else:
            print('Invalid Input')

def user_info():
    while True:
        choice = input("Press 1 for delivery, Press 2 for pickup: ")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            break

def main():
    print("Welcome to the Pizza Ordering System!")
    name = customer_name()
    phone = phone_number()
    user_info()
    pizza_list()
    print(f"Customer Name: {name}, Phone: {phone}")
    print(f"Total number of premium pizzas: {pizza_dict['num_premium_pizzas']}")
    print(f"Total number of gourmet pizzas: {pizza_dict['num_gourmet_pizzas']}")

if __name__ == "__main__":
    main()

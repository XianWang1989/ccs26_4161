
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme",
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"
]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "selected_pizzas": 0,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

def customer_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.isalpha() and name.strip():
                return name
            else:
                print("Error: Name must be a non-empty string.")
        except Exception as e:
            print(f"Error: {e}")

def delivery_details():
    while True:
        try:
            address = input("Please enter your delivery address: ")
            if address.strip():
                return address
            else:
                print("Error: Address must not be empty.")
        except Exception as e:
            print(f"Error: {e}")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number (digits only): "))
            if len(str(phone_number)) >= 7:  # Checking if phone number has at least 7 digits
                return phone_number
            else:
                print("Error: Phone number must be at least 7 digits long.")
        except ValueError:
            print("Error: Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 5.')

    for idx, pizza in enumerate(premium_pizzas, start=1):
        print(f"{idx}. {pizza}")

    for idx, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{idx}. {pizza}")

    return num_pizzas

def user_info():
    while True:
        choice = input("Press 1 for delivery, Press 2 for pickup: ")
        if choice == "1":
            delivery_details()
            break
        elif choice == "2":
            pizza_list()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def main():
    name = customer_name()
    phone = get_phone_number()
    print(f"Customer Name: {name}\nPhone Number: {phone}")

    user_info()

if __name__ == "__main__":
    main()

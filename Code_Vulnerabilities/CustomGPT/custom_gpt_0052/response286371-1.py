
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme",
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ",
    "BBQ Chicken", "Hellfire"
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
        customer_name = input("Please enter your name: ")
        if customer_name.strip():
            return customer_name
        else:
            print("Error: You must enter a name!")

def delivery_details():
    while True:
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address.strip():
            return delivery_address
        else:
            print("Error: You must enter a delivery address!")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n"))
            if 1000000 <= phone_number <= 9999999:  # Adjust for valid lengths
                return phone_number
            else:
                print("Error: Phone number must be a 7-digit number!")
        except ValueError:
            print("Error: Phone number must be an integer!")

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input("How many pizzas would you like (max of 5): "))
        except ValueError:
            print("Invalid input, please enter a number.")

    for pizza in premium_pizzas:
        print(pizza)

    for pizza in gourmet_pizzas:
        print(pizza)

    return num_pizzas

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery, press 2 for pickup: ")
        if get_user_info == "1":
            delivery_details()
            break
        elif get_user_info == "2":
            break
        else:
            print("Invalid input, please select 1 or 2.")

# Main program
if __name__ == "__main__":
    name = customer_name()
    phone_number = get_phone_number()
    num_pizzas = pizza_list()
    user_info()

    print(f"\nCustomer Name: {name}")
    print(f"Phone Number: {phone_number}")
    print(f"Number of Pizzas: {num_pizzas}")

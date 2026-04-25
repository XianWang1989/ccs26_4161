
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", 
                  "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", 
                  "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
                  "BBQ Chicken", "Hellfire"]

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
        if customer_name.strip():  # Check if input is not empty
            return customer_name
        print("Error: You must enter something!")

def delivery_details():
    while True:
        delivery_address = input("Please enter your delivery address: ")
        if delivery_address.strip():  # Check if input is not empty
            return delivery_address
        print("Error: You must enter something!")

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number (digits only): "))
            if len(str(phone_number)) >= 7:  # Ensure valid phone number length
                return phone_number
            else:
                print("Phone number must be at least 7 digits.")
        except ValueError:
            print("Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid input, please enter a number.')

    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    selected_pizzas = []
    for _ in range(num_pizzas):
        selected = int(input('Select Your Premium Pizza (by number): ')) - 1
        if 0 <= selected < len(premium_pizzas):
            selected_pizzas.append(premium_pizzas[selected])
        else:
            print('Invalid selection. Please try again.')

    pizza_dict['num_premium_pizzas'] += len(selected_pizzas)
    return selected_pizzas

def user_info():
    while True:
        get_user_info = input("Press 1 for delivery, Press 2 for pickup: ")
        if get_user_info == "1":
            delivery_details()
            break
        elif get_user_info == "2":
            pizza_list()
            break
        else:
            print("Invalid input, please enter 1 or 2.")

if __name__ == "__main__":
    name = customer_name()
    phone = get_phone_number()
    user_info()

    # Printing out all gathered information at the end
    print(f"Customer Name: {name}")
    print(f"Phone Number: {phone}")
    print(f"Number of Premium Pizzas: {pizza_dict['num_premium_pizzas']}")

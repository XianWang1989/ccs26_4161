
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

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
            name = str(input("Please enter your name: "))
            if name.isdigit():
                print("Error: Name cannot be a number!")
                continue
            break  # valid name entered
        except Exception as e:
            print(f"Error: {e}")
    print(f"Hello, {name}!")
    return name

def delivery_details():
    while True:
        try:
            delivery_address = str(input("Please enter your delivery address: "))
            if delivery_address == "":
                raise ValueError("Address cannot be blank.")
            break  # valid address entered
        except ValueError as e:
            print(f"Error: {e}")
    return delivery_address

def get_phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number (digits only): "))
            if phone_number < 1000000:  # Example validation (must be at least 7 digits)
                print("Phone number must be at least 7 digits long.")
                continue
            return phone_number
        except ValueError:
            print("Phone number must be an integer only.")

def pizza_list():
    num_pizzas = -1
    while (num_pizzas <= 0) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
            if num_pizzas <= 0 or num_pizzas > 5:
                raise ValueError("Invalid number of pizzas")
        except ValueError as e:
            print(f"Error: {e}")

    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    # Code for selecting pizzas will go here...

def user_info():
    while True:
        try:
            get_user_info = str(input("Press 1 for delivery, Press 2 for pickup: "))
            if get_user_info not in ["1", "2"]:
                raise ValueError("Invalid option.")
            if get_user_info == "1":
                delivery_details()
                break
            elif get_user_info == "2":
                pizza_list()
                break
        except ValueError as e:
            print(f"Error: {e}")

# Main flow
if __name__ == "__main__":
    name = customer_name()
    phone_number = get_phone_number()
    user_info()



premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham" , "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

def customer_name():
    while True:
        try:
            name = str(input("Please enter your name: "))
            if name.strip():  # Check if not empty
                return name
            else:
                print("Error: Name cannot be empty!")
        except Exception as e:
            print(f"Error: {e}")

def delivery_details():
    while True:
        try:
            address = str(input("Please enter your delivery address: "))
            if address.strip():  # Check if not empty
                return address
            else:
                print("Error: Address cannot be empty!")
        except Exception as e:
            print(f"Error: {e}")

def phone_number():
    while True:
        try:
            number = int(input("Please enter your phone number (digits only): "))
            if len(str(number)) >= 7:  # Minimum valid phone number length
                return number
            else:
                print("Error: Phone number must have at least 7 digits.")
        except ValueError:
            print("Phone number must be an integer.")

def pizza_list():
    num_pizzas = -1
    while (num_pizzas < 0) or (num_pizzas > 5):
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    selected_pizzas = []
    # Your pizza selection logic goes here...

    return selected_pizzas  # Return the selected pizzas

def main():
    user_data = []
    user_data.append(customer_name())
    user_data.append(delivery_details())
    user_data.append(phone_number())
    user_data.append(pizza_list())

    print("User Data: ", user_data)  # Print all user info at the end

if __name__ == "__main__":
    main()

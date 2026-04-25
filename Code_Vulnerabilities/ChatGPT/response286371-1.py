
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham" , "Vegetriano" ]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00, "selected_pizzas": 0, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

def customer_name():
    while True:
        try:
            name = str(input("Please enter your name: "))
            if name.isdigit():
                print("Error: Name can't be a number!")
                continue
            return name
        except Exception as e:
            print("Error: You must enter something!")

def delivery_details():
    while True:
        try:
            delivery_address = str(input("Please enter your delivery address: "))
            if delivery_address == "":
                print("Error: You must enter a delivery address!")
                continue
            return delivery_address
        except Exception as e:
            print("Error: You must enter something!")

def phone_number():
    while True:
        try:
            phone_number = int(input("Please enter your phone number:\n\t"))
            if phone_number < 0 or len(str(phone_number)) < 7:
                print("Error: Phone number must be a positive integer with at least 7 digits!")
                continue
            return phone_number
        except ValueError:
            print("Error: Phone number must be a number!")

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    display_pizza_options(num_pizzas)

def display_pizza_options(num_pizzas):
    print('\n==Premium Pizzas==\n')
    for i in range(1, len(premium_pizzas) + 1):
        print(f"{i}. {premium_pizzas[i - 1]}")

    print('\n==Gourmet Pizzas==\n')
    for i in range(1, len(gourmet_pizzas) + 1):
        print(f"{i}. {gourmet_pizzas[i - 1]}")

    # ... (Add the pizza selection logic here, similar to your original code)


def user_info():
    while True:
        user_choice = str(input("Press 1 for delivery or 2 for pickup: "))
        if user_choice == "1":
            delivery_details()
            break
        elif user_choice == "2":
            pizza_list()
            break
        else:
            print("Invalid choice, please try again.")

# Main Program Execution
def main():
    name = customer_name()
    phone = phone_number()

    # You can add more functions if necessary ...

    user_info()

    # Example of how to print out variables at the end
    print(f"Customer Name: {name}, Phone Number: {phone}")

if __name__ == "__main__":
    main()

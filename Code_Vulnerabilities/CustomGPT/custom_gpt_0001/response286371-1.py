
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

# List to store user information
user_info_list = []

def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ")
    user_info_list.append(name)  # Append user name to list
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        delivery_address = input("Please enter your delivery address: ")
    user_info_list.append(delivery_address)  # Append address to list

def get_phone_number():
    phone_number = ""
    while True:
        phone_number = input("Please enter your phone number:\n\t")
        if phone_number.isdigit() and len(phone_number) >= 7:
            break
        print("Phone number must be at least 7 digits and numeric only.")
    user_info_list.append(phone_number)  # Append phone number to list
    return phone_number

def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    pizza_dict = {"premium_pizza_price": 8.50, "gourmet_pizza_price": 5.00,
                  "selected_pizzas": 0, "num_premium_pizzas": 0, "num_gourmet_pizzas": 0}

    # Display pizzas
    print('\n==Premium Pizzas==\n')
    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    print('\n==Gourmet Pizzas==\n')
    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

    # Select pizzas (omitting the pizza selection code for brevity)
    return pizza_dict

# Main interaction
if __name__ == "__main__":
    customer_name()
    delivery_details()
    get_phone_number()
    pizza_dict = pizza_list()

    # Print all collected user information
    print("User Information Collected:")
    for info in user_info_list:
        print(info)

    # Add receipt calculations as needed here

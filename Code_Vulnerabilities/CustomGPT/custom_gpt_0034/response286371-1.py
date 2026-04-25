
premium_pizzas = ["Supreme Cheese", "The Legendary pizza", "Pentakill supreme", "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

# Function for customer name
def customer_name():
    name = ""
    while name == "":
        name = input("Please enter your name: ")
    return name

# Function for phone number
def phone_number():
    phone = 0
    while phone < 1000000 or phone > 9999999:  # Assuming a 7-digit phone number
        try:
            phone = int(input("Please enter your phone number (7 digits): "))
        except ValueError:
            print("Phone number must be 7 digits.")
    return phone

# Function for pizza selection
def pizza_list():
    num_pizzas = -1
    while num_pizzas < 1 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (1 to 5): '))
        except ValueError:
            print('Invalid input, please enter a number between 1 and 5.')

    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")

    for i in range(len(gourmet_pizzas)):
        print(f"{i + 1}. {gourmet_pizzas[i]}")

# Main function to execute the flow
def main():
    name = customer_name()
    phone = phone_number()  
    pizza_list()

    print(f"\nCustomer Name: {name}")
    print(f"Phone Number: {phone}")

main()

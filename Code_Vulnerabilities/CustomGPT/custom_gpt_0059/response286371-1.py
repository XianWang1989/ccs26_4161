
premium_pizzas = [
    "Supreme Cheese", "The Legendary pizza", "Pentakill supreme",
    "Teeto shroomo supreme", "The volcanic rengar", "Cheese and Ham", 
    "Vegetriano"
]
gourmet_pizzas = [
    "Flame Gorilla", "Snazzy chicken", "Intergalactic BBQ", 
    "BBQ Chicken", "Hellfire"
]

pizza_dict = {
    "premium_pizza_price": 8.50,
    "gourmet_pizza_price": 5.00,
    "num_premium_pizzas": 0,
    "num_gourmet_pizzas": 0
}

# Function to get the customer's name
def customer_name():
    name = ""
    while name == "":
        try:
            name = input("Please enter your name: ")
        except Exception:
            print("Error! You must enter a valid name.")
    return name

# Function to get delivery details
def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        try:
            delivery_address = input("Please enter your delivery address: ")
        except Exception:
            print("Error! You must enter a valid address.")
    return delivery_address

# Function to get the phone number
def get_phone_number():
    phone_number = ""
    while len(phone_number) < 7:
        try:
            phone_number = input("Please enter your phone number (at least 7 digits): ")
            if not phone_number.isdigit():
                raise ValueError
        except ValueError:
            print("Phone number must be at least 7 digits and only contain numbers.")
    return phone_number

# Function to handle pizza selection
def pizza_list():
    num_pizzas = 0
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input("How many pizzas would you like (max of 5): "))
        except ValueError:
            print("Invalid Input")

    # Print pizza options
    print('\n==Premium Pizzas==\n')
    for i, pizza in enumerate(premium_pizzas, start=1):
        print(f"{i}. {pizza}")

    print('\n==Gourmet Pizzas==\n')
    for i, pizza in enumerate(gourmet_pizzas, start=1):
        print(f"{i}. {pizza}")

    # Get selected pizzas
    for _ in range(num_pizzas):
        selected = input('Select Your Pizza (Enter "next" to finish): ')
        if selected == "next":
            break
        else:
            try:
                selected = int(selected)
                if selected <= 0 or selected > len(premium_pizzas):
                    print("Invalid Input")
                else:
                    pizza_dict['num_premium_pizzas'] += 1
            except ValueError:
                print('Invalid Input')

# Main program execution
def main():
    name = customer_name()
    phone = get_phone_number()
    address = delivery_details()
    pizza_list()

    print(f"Customer Name: {name}, Phone: {phone}, Address: {address}")
    print(f"Total premium pizzas ordered: {pizza_dict['num_premium_pizzas']}")

main()

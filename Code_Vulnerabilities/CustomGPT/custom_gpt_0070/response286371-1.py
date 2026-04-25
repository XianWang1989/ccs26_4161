
premium_pizzas = ["Supreme Cheese", "The Legendary Pizza", "Pentakill Supreme", "Teeto Shroomo Supreme", "The Volcanic Rengar", "Cheese and Ham", "Vegetriano"]
gourmet_pizzas = ["Flame Gorilla", "Snazzy Chicken", "Intergalactic BBQ", "BBQ Chicken", "Hellfire"]

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
    return name

def delivery_details():
    delivery_address = ""
    while delivery_address == "":
        delivery_address = input("Please enter your delivery address: ")
    return delivery_address

def get_phone_number():
    phone_number = -1
    while phone_number < 0 or phone_number < 7:
        try:
            phone_number = int(input("Please enter your phone number (7+ digits): "))
        except ValueError:
            print("Phone number must be an integer only.")
    return phone_number

def pizza_list():
    num_pizzas = -1
    while num_pizzas <= 0 or num_pizzas > 5:
        try:
            num_pizzas = int(input('How many pizzas would you like (max of 5): '))
        except ValueError:
            print('Invalid Input')

    for i in range(len(premium_pizzas)):
        print(f"{i + 1}. {premium_pizzas[i]}")
    print('\nEnter "next" to move on to Gourmet Pizzas.\n')

    for _ in range(num_pizzas):
        selected = ""
        while True:
            selected = input('Select Your Premium Pizza (or type "next"): ')
            if selected.strip().lower() == 'next':
                break
            try:
                selected = int(selected)
                if selected <= 0 or selected > len(premium_pizzas):
                    print('Invalid Input')
                else:
                    pizza_dict['num_premium_pizzas'] += 1
                    break
            except ValueError:
                print('Invalid Input')

    # You can implement a similar loop for gourmet pizzas

def main():
    name = customer_name()
    address = delivery_details()
    phone = get_phone_number()
    pizza_list()

    # You can print out the collected info at the end
    print(f"Customer Name: {name}")
    print(f"Delivery Address: {address}")
    print(f"Phone Number: {phone}")
    print(f"Total Premium Pizzas: {pizza_dict['num_premium_pizzas']}")

# Start the program
main()

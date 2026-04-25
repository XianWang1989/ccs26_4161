
def run():
    name = input('Please Enter your question: ').lower()
    carLists = ['car', 'bus', 'bike']  # Sample car list
    if any(car in name for car in carLists):
        print('You found the vehicle here!')

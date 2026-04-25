
def run():
    name = input('Please enter your question about cars: ').lower()
    carLists = ['car', 'truck', 'bike']
    if any(car in name for car in carLists):
        print('You mentioned a vehicle!')

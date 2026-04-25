
# MODULE2.py
def main():
    name = input('Please enter your question: ').lower()
    car_lists = ['car', 'truck', 'bicycle']
    if any(car in name for car in car_lists):
        print('You found a type of vehicle!')
        name3 = input('What is your favorite vehicle? ').lower()
        responses = {
            'car': 'Cars are great!',
            'truck': 'Trucks are powerful!',
            'bicycle': 'Bicycles are eco-friendly!'
        }
        print(responses.get(name3, 'I do not recognize that vehicle.'))

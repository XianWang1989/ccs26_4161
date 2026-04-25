
def run_module():
    name = input('Please enter your question: ').lower()
    vehicle_lists = ['car', 'bike']  # Example list
    if any(vehicle in name for vehicle in vehicle_lists):
        print('You mentioned a vehicle!')

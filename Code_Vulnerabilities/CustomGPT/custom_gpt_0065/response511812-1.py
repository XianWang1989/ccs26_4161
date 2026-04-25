
def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    results = []
    for line in lines:
        name, *scores = line.strip().split(',')
        scores = list(map(int, scores))
        average_score = sum(scores) / len(scores)
        results.append((name, average_score))
    return results

def main():
    file_path = "Class1.txt"
    data = read_data(file_path)

    for name, avg in data:
        print(f"{name}: {avg:.2f}")

if __name__ == "__main__":
    main()

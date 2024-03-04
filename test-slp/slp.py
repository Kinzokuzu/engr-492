import csv

def get_data(f_name):
    """
    Read data from a csv file and return it as a list of lists.
    """
    data = []
    with open(f_name, 'r') as file:
        reader = csv.reader(file)

        for row in reader:
            data.append(row)

    return data

def print_data(data):
    """
    Print the data to the console.
    """
    for row in data:
        for i in range(len(row)):
            if i % 3 == 0:
                print()

            print(row[i], end=' ')

def predict(input, weights):
    threshold = 0.0
    activation = 0.0
    for i,w in zip(input, weights):
            activation += i*w

    return 1.0 if activation >= threshold else 0.0


data = get_data('numbers.csv')
w_matrix = data.copy() # weights matrix
output = [] # 1x10 matrix

for d in data:
    for w in w_matrix:
        output.append(predict(d[:-1], w))

print_data(output)



import csv
import matplotlib.pyplot as plt

# Read the data
with open('putty.log', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

plt.plot(data)

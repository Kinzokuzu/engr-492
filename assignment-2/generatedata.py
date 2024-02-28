import random

# header
print('Height (meters),Weight (kg),health index')

# BMI calculation: weight (kg) / height^2 (m)
IDEAL_HEIGHT = 1.75
IDEAL_WEIGHT = 67.375
IDEAL_BMI = 22

def generate_data(ideal, count, outer=0.0, inner=0.0):
    # calculate the range of values
    o_bmi = ideal + ideal * outer
    i_bmi = ideal - ideal * inner

    # generate the data
    data = []
    for i in range(count):
        bmi = 0
        if outer < 1:
            bmi = random.uniform(o_bmi, i_bmi)
        else:
            bmi = random.uniform(i_bmi, o_bmi)
        height = random.uniform(1.5, 2.0)
        weight = bmi * height**2
        health_index = 0

        if outer == 0.15 or outer == -0.15:
            health_index = 1
        elif outer > 0.15 or outer < -0.15:
            health_index = 2

        if bmi < ideal:
            health_index = health_index * -1
        

        data.append((height, weight, health_index))

    return data

def print_data(data):
    for d in data:
        print('{:4.3f}'.format(d[0]),',',
              '{:5.3f}'.format(d[1]), ',',
              d[2], sep='')

print_data(generate_data(IDEAL_BMI, 5, 0.05))
print_data(generate_data(IDEAL_BMI, 5, -0.05))
print_data(generate_data(IDEAL_BMI, 10, 0.15, 0.05))
print_data(generate_data(IDEAL_BMI, 10, -0.15, -0.05))
print_data(generate_data(IDEAL_BMI, 10, 0.25, 0.15))
print_data(generate_data(IDEAL_BMI, 10, -0.25, -0.15))

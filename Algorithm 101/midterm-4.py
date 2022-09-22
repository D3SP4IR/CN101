# Phuree Phenhiran 6510742502

num_of_wheel = int(input('Please input number of wheels of your vehicle: ')) 
distance = int(input('Distance of your toll way (km): '))

cost = 0

if distance < 10:
    cost = 40 if num_of_wheel==4 else 60 if 5<=num_of_wheel<=10 else 80
elif 10 <= distance <= 50:
    cost = 50 if num_of_wheel==4 else 70 if 5<=num_of_wheel<=10 else 90
else:
    cost = 60 if num_of_wheel==4 else 80 if 5<=num_of_wheel<=10 else 100

print(f'Total cost of your toll is {cost} THB')
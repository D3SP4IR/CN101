# 6510742502 Phuree Phenhiran

PI = 3.14

print('1. Circle Area\n2. Circumference')
choice = int(input('Your choice: '))
radius = float(input('Input radius: '))

if choice == 1:
    area = PI * radius ** 2
    print(f'Circle Area: {area:.2f}')

else:
    circumference = 2 * PI * radius
    print(f'Circumference: {circumference:.2f}')
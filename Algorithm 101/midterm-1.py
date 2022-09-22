# Phuree Phenhiran 6510742502

z = 0
x = int(input('Input x: '))
y = int(input('Input y: '))

if x % y != 0:
    y -= 2
    z += x

z += 1

print(f'z = {z}\ny = {y}')
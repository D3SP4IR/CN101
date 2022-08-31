# -- using ternary if-else and bitwise operation method --
# num = int(input('Input an integer: '))
# print('Odd' if num&1 else 'Even')

# -- general method --
num = int(input('Input an integer: '))

if num%2==0:
    print('Even')
else:
    print('Odd')
# Phuree Phenhiran 6510742502

h = int(input('Enter parking hours (>=0): '))
m = int(input('Enter parking minutes (0-59): '))

fee = 0 if h==0 and m<30 else 20*(h+bool(m))

print(f'Parking for {h} hour and {m} min. The fee is {fee} baht.')
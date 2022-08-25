money = int(input())
coin = [1000, 500, 100, 50, 20, 5, 1]

for c in coin:
    print(c, money//c)
    money %= c
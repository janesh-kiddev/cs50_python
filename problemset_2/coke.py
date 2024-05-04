price = 50
total = 0
coins = [25, 10, 5]

while price > 0:
    print(f"Amount Due: {price}")
    pay = int(input("Insert Coin: "))
    if pay in coins:
        price = price - pay
        total = total + pay

if total >= price:
    print(f"Change Owed: {total - 50}")

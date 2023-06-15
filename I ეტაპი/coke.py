def main():
    amount = 50
    coins = [5, 10, 25]
    while(amount > 0):
        print(f"Amount Due: {amount}")
        user_input = int(input("Insert Coin: "))
        if user_input in coins:
            amount -= user_input
    print(f"Change Owed: {abs(amount)}") 

main()   


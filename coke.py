def main():
    print("Amount Due: 50")
    balance = 50

    while balance > 0:
        insertcoin = int(input("Insert Coin: "))

        if insertcoin in [5, 10, 25]:
            balance -= insertcoin

            if balance > 0:
                # insertcoin = int(input("Insert Coin: "))
                print(f"Amount Due: {balance}")
                # return insertcoin, balance
            else:
                change = abs(balance)
                print(f"Change Owed: {change}")
                break
        else:
            print(f"Amount Due: {balance}")
            # insertcoin = int(input("Insert Coin: "))
            # return insertcoin, balance



        # else:
        #     print("Invalid coin denomination. Please insert 5, 10, or 25 only.")

main()

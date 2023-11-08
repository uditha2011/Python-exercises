def main():
    order = {}
    quantity = 1

    while True:
        try:
            user_input = input().strip().upper()
            
            if user_input in order:
                order[user_input] += quantity

            else:
                order[user_input] = quantity
            
        
        except KeyboardInterrupt:
            print()
            for quantity, user_input in order.items():
                print(user_input, quantity)
            break

        except EOFError:
            print()
            for user_input, quantity in order:
                print(user_input, quantity)
            break
        

if __name__ == "__main__":
    main()



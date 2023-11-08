def main():

    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0
    while True:
        # if keyboard.read_key() == "x": 
        #     break

        try:
            food_name = input("Item: ").title()

            if food_name in menu:
                total = total + float(menu.get(food_name))
                print(f"Total: ${total:.2f}")
            # elif  show(key):
            #     break
        except (ValueError , KeyboardInterrupt):
            break

        except EOFError:
            # print('exiting')
            break



if __name__ == "__main__":
    main()
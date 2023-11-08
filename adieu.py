import inflect
import re
p = inflect.engine()


def main():
    list = []
    # print('test 1111')
    while True:
        try:
            userinput = input("Name: ").strip().title()
            list.append(userinput)

            # JOIN WORDS INTO A LIST:

            mylist = p.join(list)
            # print(list)
            



        except EOFError:
            print("Adieu, adieu, to", mylist)
            break

        except KeyboardInterrupt:
            print("Adieu, adieu, to", mylist)
            break


main()
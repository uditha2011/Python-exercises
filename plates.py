def main():
    plate = input("Plate: ")
    # plate = "CS55"
    print(plate)

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    # if not s.isalpha():
    #     return False

    # Check whether only numbers and letters are contained in the input
    if not s.isalnum():
        print("test1")
        return False
    else:
        # Check whether the length is between 2 and 6 characters
        if 2 <= len(s) <= 6:
            print("test2")
            return startingWithLetters(s)
        else:
            print("test3")
            return False

def startingWithLetters(s):
    # Check whether the first 2 characters are letters

    firsttwochar = s[:2]
    # print(s[:2])
    if s.isalpha():
        print("test4")
        return True
    else:
        if firsttwochar.isalpha():
            print("test5")
            return numAtTheEnd(s[2:])
        else:
            print("test6")
            return False

def numAtTheEnd(lastFourStr):
    # Verify that numbers are at the end
    print(range(len(lastFourStr)-1))

    for i in range(len(lastFourStr)-1):
        print(i, lastFourStr[i])

        if lastFourStr[i].isdigit():
            print("test7")
            if lastFourStr[i + 1].isalpha():
                print("test8")
                return False
            elif lastFourStr[i + 1].isdigit():
                print("test9")
                # print(i)
                if lastFourStr[i] == '0':
                    print("test10")
                    return False
                elif lastFourStr[i] != '0':
                    i = i + 1
                    # print(i)
                    print("test11")
                    numAtTheEnd(lastFourStr)
                    # return i
                else:
                    print("test12")
                    return True
            else:
                print("test13")
                return False
        else:
            print("test14")
            i = i + 1

if __name__ == "__main__":
    main()

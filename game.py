import random
import sys

while True:
    try:
        userinput = input("Level: ")
        # print(userinput)


        if userinput.isnumeric() is True:
            # print('test 111')
            # print(int(userinput))
            if int(userinput) > 0:
                # print('test 222')
                numbers = random.randint(1,int(userinput))
                # print('test 333')
                print(numbers)

                while True:
                
                    inputguess = input("Guess: ")

                    if inputguess.isnumeric() is True:
                        
                        if int(inputguess) == numbers:
                            print('Just right!')
                            sys.exit()
                        elif int(inputguess) < numbers:
                            print('Too small!')
                            
                        elif int(inputguess) > numbers:
                            print('Too large!')
                            
                    else:
                        pass

                

    except KeyboardInterrupt:
        break

    except EOFError:
        break
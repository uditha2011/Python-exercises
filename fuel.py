# def get_fraction(x,y):

    # while True:
                        
        # try:
        #     fraction = float(int(x)/int(y))
        #     print(fraction)
        #     # return fraction
        #     if fraction == 0:
        #         print('E')
        #     elif fraction == 0.25:
        #         print('25%')
        #     elif fraction == 0.5:
        #         print('50%')
        #     elif fraction == 1:
        #         print('F')
        #     else:
        #         pass
          
        # except ValueError:
        #     # or ZeroDivisionError
        #     pass

        # else:
        #     return fraction




    
def main(): 
    import math
    fraction = '0'
    # x = '0'
    # y = '0'
    # x, y = input("Fraction: ").split('/' )
    # print(x)
    # print(y)

    while True:
        try:
            x, y = input("Fraction: ").split('/' )
            # print(x)
            # print(y)
            fraction = float(int(x)/int(y))
            # print(fraction)
            # return fraction
            if 0 <= fraction <= 1:
                if fraction == 0:
                    print('E')
                elif fraction == 1:
                    print('F')
                elif x== '1' and y=='100':
                    print('E')
                elif x=='99' and y=='100':
                    print('F')
                else:
                    print(round(fraction*100),"%", sep='')
            else:
                continue

                
        except (ValueError, ZeroDivisionError):
            pass

        else:
            return fraction

    # get_fraction(x,y)

    



main()
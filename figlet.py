from pyfiglet import Figlet
import sys

try:
    if len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        selected_font = sys.argv[2]
        f = Figlet(font= selected_font)
        userinput=input("Input: ")
        print('Output: ', f.renderText(userinput))

    else:
        sys.exit('Invalid usage')

except KeyboardInterrupt:
    sys.exit()

# except:
#     print('test 12')
#     sys.exit()
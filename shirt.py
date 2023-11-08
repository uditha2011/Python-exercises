from ast import Param
import sys
from PIL import Image
import PIL

def main():
    try:
        if len(sys.argv) <= 2:
            print("Too few command-line arguments")
            sys.exit(1)

        elif len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit(1)

        elif len(sys.argv) == 3 and (((sys.argv[1].lower().endswith('.jpg') and sys.argv[2].lower().endswith('.jpg'))) or ((sys.argv[1].lower().endswith('.jpeg') and sys.argv[2].lower().endswith('.jpeg'))) or ((sys.argv[1].lower().endswith('.png]') and sys.argv[2].lower().endswith('.png')))):
            
            # print('ok')

            with Image.open(sys.argv[1]) as file:
                shirt = Image.open("shirt.png")
                size=shirt.size
                file2 = PIL.ImageOps.fit(file,size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))
                file2 = file2.copy()
                file2.paste(shirt, (0,0), shirt)
                file2.save(sys.argv[2], format=None)


        elif len(sys.argv) == 3: 
            
            try:
                text1,text2 = sys.argv[1].lower().split('.')
                text3,text4 = sys.argv[2].lower().split('.')

                if text2 != text4:
                    print('Input and output have different extensions')
                    sys.exit(1)
                    
            except:
                print("Invalid input")
                sys.exit(1)
            # and (sys.argv[1].lower().endswith(sys.argv[2]) or sys.argv[2].lower().endswith(sys.argv[1])):

            
        # else:
        #     print("Invalid input")
        #     sys.exit(1)
        

    except FileNotFoundError:
        print(f'Could not read {sys.argv[1]}')
        sys.exit(1)

if __name__ == "__main__":
    main()
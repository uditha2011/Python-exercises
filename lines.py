import sys

def main():
    try:
        if len(sys.argv) == 1:
            print("Too few command-line arguments")
            sys.exit(1)
        elif len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit(1)
        elif len(sys.argv) == 2:
            for arg in sys.argv[1:]:
                if arg.endswith('.py') == False:
                    print("Not a Python file")
                    sys.exit(1)
                else:
                    with open(sys.argv[1], 'r') as file:
                        lines=file.readlines()
                        x = len(lines)
                        # print('Total lines:', x)

                        blank_lines = 0
                        commented_lines = 0

                        for line in lines:
                            stripped_line = line.strip()
                            # print('test 1')
                            if not stripped_line:
                                # Blank line
                                blank_lines += 1
                                # print('Blank lines: {blank_lines}')
                                # print('test 2')
                            elif stripped_line.startswith('#'):
                                # Commented line
                                commented_lines += 1
                                # print('Commented lines: {commented_lines}')
                                # print('test 3')


                    print(int(x - commented_lines - blank_lines))
                    return blank_lines, commented_lines




    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)



if __name__ == "__main__":
    main()

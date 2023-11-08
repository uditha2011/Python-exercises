import sys
from tabulate import tabulate
import csv

def main():
    try:
        if len(sys.argv) == 1:
            print("Too few command-line arguments")
            sys.exit(1)
        elif len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit(1)

        elif not sys.argv[1].endswith('.csv'):
            print("Not a CSV file")
            sys.exit(1)
            
        elif len(sys.argv) == 2:
        
        # input_file = sys.argv[1]

            with open(sys.argv[1], 'r') as file:
                reader = csv.reader(file)
                table = [row for row in reader]  # Read all the data rows into a list

                if table:
                    headers = table[0]
                    data = table[1:]
                    print(tabulate(data, headers, tablefmt="grid"))
                else:
                    print("CSV file is empty")

    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)

if __name__ == "__main__":
    main()

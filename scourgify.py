import sys
import csv

def main():
    try:
        if len(sys.argv) <= 2:
            print("Too few command-line arguments")
            sys.exit(1)

        elif len(sys.argv) > 3:
            print("Too many command-line arguments")
            sys.exit(1)

        elif len(sys.argv) == 3 and (sys.argv[1].endswith('.csv') and sys.argv[2].endswith('.csv')):
            
            firstname = []
            lastname = []
            house = []

            with open(sys.argv[1], 'r') as readfile:
                reader = csv.DictReader(readfile)
                for row in reader:
                  
                    # read 'name' column and split it to two as 'firstname' and 'lastname'
                    splitname = row['name'].split(',')
                    firstname.append(splitname[1].strip())
                    lastname.append(splitname[0].strip())
                    house.append(row['house'].strip())

            # assign the 'house' column of before.csv to a column named 'house' in after.csv 

            with open(sys.argv[2], 'w', newline='') as writefile:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(writefile, fieldnames=fieldnames)
                writer.writeheader()

                for first, last, house in zip(firstname, lastname, house):
                    writer.writerow({'first': first, 'last': last, 'house': house})


        else:
            print("Not a CSV file")
            sys.exit(1)
        

    except FileNotFoundError:
        print(f'Could not read {sys.argv[1]}')
        sys.exit(1)

if __name__ == "__main__":
    main()
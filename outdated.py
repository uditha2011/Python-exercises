MONTH = [
    ["January","01"],
    ["February","02"],
    ["March","03"],
    ["April","04"],
    ["May","05"],
    ["June","06"],
    ["July","07"],
    ["August","08"],
    ["September","09"],
    ["October","10"],
    ["November","11"],
    ["December","12"]
]

import re

def main():

    # delimiters1 = ['/']
    # delimiters2 = [' ', ',']
    month = date = year = ''

    while True:
        try:
            try:
                user_input = input("Date: ").strip()
                newparts=[]
                parts = re.split(r'[\/]', user_input)
                
                for x in parts:
                    if x != '':
                        newparts.append(x)
                print(newparts)
                print('test 1')
                month, date, year = newparts
                
                if month.isalpha():
                    pass

                elif date.isalpha():
                    pass

                elif month.isnumeric() and (int(month) < 13 and int(month) >= 0) and (int(date) < 32 and int(date) >= 0):
                    print('test 582')
                    print(year+"-"+month.zfill(2)+"-"+date.zfill(2))
                    break
                
                else:
                    print('test 3699')
                    pass
            
            except ValueError:
                print('test 989898')
                newparts=[]
                parts = re.split(r'[,]', user_input)
                
                for x in parts:
                    if x != '':
                        newparts.append(x)
                
                print('test 1-1')
                month, date, year = newparts
                print(newparts)

                if date.isalpha():
                    print('test 23-1')
                    pass

                elif (int(date) < 32 and int(date) >= 0):
                    MonthDateformat = None
                    for row in MONTH:
                        # print('test 65')
                        # print(month.title())
                        if row[0] == month.title():
                            # print('test 78')
                            # print(row[1])
                            MonthDateformat = row[1]
                            # print(MonthDateformat)
                            # print(year+"-"+MonthDateformat.zfill(2)+"-"+date.zfill(2))
                            continue
                    if MonthDateformat:
                        # print('test 1478')
                        print(year+"-"+MonthDateformat+"-"+date.zfill(2))
                        return

                
                else:
                    print('test 3699-1')
                    pass


        except EOFError:
            print('test 665')
            break

        except ValueError:
            print('test 8888')
            
            newparts=[]
            parts = re.split(r'[ ,]', user_input)
            
            for x in parts:
                if x != '':
                    newparts.append(x)
            
            print('test 1-166')
            month, date, year = newparts
            print(newparts)

            if date.isalpha():
                print('test 23-166')
                continue

            elif (int(date) < 32 and int(date) >= 0):
                MonthDateformat = None
                for row in MONTH:
                    # print('test 65')
                    # print(month.title())
                    if row[0] == month.title():
                        # print('test 78')
                        # print(row[1])
                        MonthDateformat = row[1]
                        # print(MonthDateformat)
                        # print(year+"-"+MonthDateformat.zfill(2)+"-"+date.zfill(2))
                        continue
                if MonthDateformat:
                    # print('test 1478')
                    print(year+"-"+MonthDateformat+"-"+date.zfill(2))
                    return

            
            else:
                print('test 3699-166')
                continue






            break

        except KeyboardInterrupt:
            # print('test 6879')
            break



if __name__ == "__main__":
    main()


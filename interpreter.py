expression = input("Expression: ")
array = expression.lstrip().split()

# print(array[0])
# print(array[1])
# print(array[2])

if array[1]=="+":
    z = float(array[0]) + float(array[2])
    m = round(z,1)
    print(m)
elif array[1]=="-":
    z = float(array[0]) - float(array[2])
    m = round(z,1)
    print(m)
elif array[1]=="*":
    z = float(array[0]) * float(array[2])
    m = round(z,1)
    print(m)
elif array[1]=="/":
    z = float(array[0]) / float(array[2])
    m = round(z,1)
    print(m)
else:
    print("Please enter the expression correctly")
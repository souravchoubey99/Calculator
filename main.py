print("Press 1 for Addition \n Press 2 for Subtraction \nPress 3 for Multification \n Press 4 for Divison \n Press 5 To exit the Program")

while (True):
    Value = int(input("Enter the value: "))
    print(Value)
    a = int(input("Enter the value of a : "))
    print(a)
    b = int(input("Enter the value of b : "))
    print(b)

    Add = a + b
    Sub = a - b
    Mul = a * b
    Div = a / b

    if (Value == 1):
        print(Add)
    elif (Value == 2):
        print(Sub)
    elif (Value == 3):
        print(Mul)
    elif (Value == 4):
        print(Div)
    elif(Value==5):
        break
    else:
        print("Please enter the value between 1 to 5")




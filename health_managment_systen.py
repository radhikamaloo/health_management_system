import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("Enter 1 for Exercise and 2 for Food "))
        if(c==1):
            value=input("enter the text\n")
            with open("harry-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Sucessfully written")
        elif(c==2):
            value=input("enter the text\n")
            with open("harry-fd.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Sucessfully written")


    elif k==2:
        c = int(input("Enter 1 for Exercise and 2 for Food "))
        if (c == 1):
            value = input("enter the text\n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Sucessfully written")
        elif (c == 2):
            value = input("enter the text\n")
            with open("rohan-fd.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Sucessfully written")
    elif k==3:
        c = int(input("Enter 1 for Exercise and 2 for Food "))
        if (c == 1):
            value = input("enter the text\n")
            with open("angad-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Sucessfully written")
        elif (c == 2):
            value = input("enter the text\n")
            with open("angad-fd.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Sucessfully written")
    else:
        print("Please enter a valid text")
def retreive(k):
    if k==1:
        c = int(input("Enter 1 for Exercise and 2 for Food "))
        if (c==1):
            with open("harry-ex.txt") as op:
             for i in op:
                print(i, end="")
        elif(c==2):
            with open("harry-fd.txt") as op:
             for i in op:
                print(i, end="")
    elif k==2:
        c = int(input("Enter 1 for Exercise and 2 for Food "))
        if (c == 1):
            with open("rohan-ex.txt") as op:
             for i in op:
                print(i, end="")
        elif(c==2):
            with open("rohan-fd.txt") as op:
             for i in op:
                print(i, end="")
    elif k==3:
        c = int(input("Enter 1 for Exercise and 2 for Food "))
        if (c == 1):
           with open("angad-ex.txt") as op:
            for i in op:
               print(i, end="")
        elif(c==2):
            with open("angad-fd.txt") as op:
             for i in op:
                print(i, end="")
    else:
        print("Please enter a valid text")

print("WELCOME TO THE HEALT MANAGEMENT SYSTEM")
a=int(input("enter 1 for add and 2 for retrieve"))
if a==1:
    b = int(input("Enter  1 for harry , 2 for rohan , 3 for angad"))
    take(b)
else:
    b=int(input("Enter  1 for harry , 2 for rohan , 3 for angad"))
    retreive(b)
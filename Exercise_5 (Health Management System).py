# Health Management System
# 3 clients - Harry, Rohan and Hammad

def gettime():
    import datetime
    return datetime.datetime.now()


# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


def data_retrieve():
    con = 1
    while con == 1:
        choose = int(input("Enter 1 no. to retrieve data of Harry\n"
                           "Enter 2 no. to retrieve data of Rohan\n"
                           "Enter 3 no. to retrieve data of Hammad: "))
        if choose == 1:
            choose_2 = int(input("Enter 1 to retrieve diet data of Harry\n"
                                 "Enter 2 to retrieve exercise data of Harry: "))
            if choose_2 == 1:
                f = open("harry diet.txt", "r")
                print(f.readlines())
                f.close()
            elif choose_2 == 2:
                f = open("harry exercise.txt", "r")
                print(f.readlines())
                f.close()
            else:
                print("Wrong input, Please try again.")

        elif choose == 2:
            choose_2 = int(input("Enter 1 to retrieve diet data of Rohan\n"
                                 "Enter 2 to retrieve exercise data of Rohan: "))
            if choose_2 == 1:
                f = open("rohan diet.txt", "r")
                print(f.readlines())
                f.close()
            elif choose_2 == 2:
                f = open("rohan exercise.txt", "r")
                print(f.readlines())
                f.close()
            else:
                print("Wrong input, Please try again.")

        elif choose == 3:
            choose_2 = int(input("Enter 1 to retrieve diet data of Hammad\n"
                                 "Enter 2 to retrieve exercise data of Hammad: "))
            if choose_2 == 1:
                f = open("hammad diet.txt", "r")
                print(f.readlines())
                f.close()
            elif choose_2 == 2:
                f = open("hammad exercise.txt", "r")
                print(f.readlines())
                f.close()
            else:
                print("Wrong input, Please try again.")

        else:
            print("Wrong input, Please try again.")

        con = int(input("Do you want to retrieve any more details? \n1. Yes \n2. No"))


def data_enter():
    choose = int(input("Enter 1 no. to enter data of Harry\n"
                       "Enter 2 no. to enter data of Rohan\n"
                       "Enter 3 no. to enter data of Hammad: "))
    con = 1
    if choose == 1:
        while con == 1:
            choose_2 = int(input("Enter 1 to enter diet data of Harry\n"
                                 "Enter 2 to enter exercise data of Harry: "))
            if choose_2 == 1:
                f = open("harry diet.txt", "a")
                data = input("Enter what has Harry eaten?\n")
                f.write(str(gettime()) + " " + data + "\n")
                f.close()
                con = int(input("Do you want to log more for Harry? \n1. Yes \n2. No"))
            elif choose_2 == 2:
                f = open("harry exercise.txt", "a")
                data = input("What workout does Harry did?\n")
                f.write(str(gettime()) + " " + data + "\n")
                f.close()
                con = int(input("Do you want to log more for Harry? \n1. Yes \n2. No"))
            else:
                print("Wrong input, Please try again.")

    elif choose == 2:
        while con == 1:
            choose_2 = int(input("Enter 1 to enter diet data of Rohan\n"
                                 "Enter 2 to enter exercise data of Rohan: "))
            if choose_2 == 1:
                f = open("rohan diet.txt", "a")
                data = input("Enter what has Rohan eaten?\n")
                f.write(str(gettime()) + " " + data + "\n")
                f.close()
                con = int(input("Do you want to log more for Rohan? \n1. Yes \n2. No"))
            elif choose_2 == 2:
                f = open("rohan exercise.txt", "a")
                data = input("What workout does Rohan did?\n")
                f.write(str(gettime()) + " " + data + "\n")
                f.close()
                con = int(input("Do you want to log more for Rohan? \n1. Yes \n2. No"))
            else:
                print("Wrong input, Please try again.")

    elif choose == 3:
        while con == 1:
            choose_2 = int(input("Enter 1 to enter diet data of Hammad\n"
                                 "Enter 2 to enter exercise data of Hammad: "))
            if choose_2 == 1:
                f = open("hammad diet.txt", "a")
                data = input("Enter what has Hammad eaten?\n")
                f.write(str(gettime()) + " " + data + "\n")
                f.close()
                con = int(input("Do you want to log more for Hammad? \n1. Yes \n2. No"))
            elif choose_2 == 2:
                f = open("hammad exercise.txt", "a")
                data = input("What workout does Hammad did?\n")
                f.write(str(gettime()) + " " + data + "\n")
                f.close()
                con = int(input("Do you want to log more for Hammad? \n1. Yes \n2. No"))
            else:
                print("Wrong input, Please try again.")

    else:
        print("Wrong input, Please try again.")


print("Welcome to Health care Management System\n")
operation = int(input("Enter 1 number to retrieve data of clients \nand\n"
                      "2 number to enter data of the client: "))
if operation == 1:
    data_retrieve()
elif operation == 2:
    data_enter()
else:
    print("Wrong input, Please try again.")

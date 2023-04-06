import os
def readStudents():
    studentList = []
    outfile = open("Kezz.txt", "r"
    f = outfile.read()
    print(f)
    for line in outfile:
        line = line.rstrip("\n")
        line = line.split("---")
        studentList.append({"rNo":line[0], "fName":line[1], "lName":line[2], "cName":line[3], "average":line[4]})
    outfile.close()
    return studentList

def addStudent(studentList,rNo, fName, lName, cName, average):
    student = {"Reg No":rNo, "First Name":fName, "Last Name":lName, "Course Name":cName, "Average":average}
    studentList.append(student)
    return studentList


def removeStudent():
    outfile = open("kezz.txt", "r")
    temp = open("hold.txt", "w")
    rNo = input("Enter the registration you want to delete>>")

    s = '  '
    while (s):
        s = outfile.readline()
        L = s.split("   ")
        if rNo in L:
            if len(s) > 0:
                if L[0] != rNo:
                    temp.write(s)
        else:
            print("!!!!That registration number does not exist")
    temp.close()
    outfile.close()
    os.remove("kezz.txt")
    os.rename("hold.txt", "kezz.txt")


def saveStudents(studentList):
    outfile = open("kezz.txt", 'w')
    for student in studentList:
        print(student["rNo"], student["first name"], student["last name"], student["course name"], student["average"])
    outfile.close()

def print_menu():
    print("------------------------")
    print("Select an option")
    print("A. add a student")
    print("V read a student")
    print("Q. Quit")
    print("D. Delete a student")
    print("--------------------------")

def runprogram():
    run = True
    studentList = []
    print_menu()
    ######
    while run:
        invalidOption = False
        option = input("Select the action you want to take>>").upper()
        if option.isalpha():
            option = str(option)

            if option == 'Q':
                run = False
                print("Your process has terminated successfully")
            elif option == 'A':
                outfile = open("kezz.txt", 'a')
                rNo = input("Registration Number:")
                fName = input("First Name:")
                lName = input("Last Name:")
                cName = input("Course name:")
                average = input("Average:")

                outfile.write(rNo + "    ")
                outfile.write(fName + "    ")
                outfile.write(lName + "    ")
                outfile.write(cName + "    ")
                outfile.write(average + "    " + "\n")
                outfile.close()
                addStudent(studentList, rNo, fName, lName, cName, average)
            elif option == 'D':


                removeStudent()
            elif option == 'V':
                studentList = readStudents()
            else:
                invalidOption = True
            if invalidOption:
                print("Invalid option")

runprogram()
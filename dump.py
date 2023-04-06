import os
def print_menu():
    print("------------------------")
    print("Select an option")
    print("A. register a student")
    print("R read a student")
    print("V. Update a student")
    print("D. Delete a student")
    print("--------------------------")


while True:
    print_menu()
    option = input("please make a choice>>")


    if option == "A":
        outfile = open("chege.txt", 'a')
        #details = ('rNo', '   ', 'fName', '   ', 'lName', '   ', 'cName', '    ', 'average' + "\n")
        rNo = input("Registration Number:")
        fName = input("First Name:")
        lName = input("Last Name:")
        cName = input("Course name:")
        average = input("Average:")
        #outfile.writelines(details)

        outfile.write(rNo + "    ")
        outfile.write(fName + "    ")
        outfile.write(lName + "    ")
        outfile.write(cName + "    ")
        outfile.write(average + "    " + "\n")
        outfile.close()
    elif option == "R":
        outfile = open("chege.txt", 'r')
        f =  outfile.readlines()
        print(f)
    elif option == "V":
        outfile = open("chege.txt", 'a')
        fName = input("First Name:")
        lName = input("Last Name:")
        cName = input("Course name:")
        rNo = input("Registration Number")

        outfile.write(fName + "    ")
        outfile.write(lName + "    ")
        outfile.write(cName + "    ")
        outfile.write(rNo + "    " + "\n")
        outfile.close()

    elif option == "D":
        outfile = open("chege.txt", "r")
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
        os.remove("chege.txt")
        os.rename("hold.txt", "chege.txt")

    else:
        print("Invalid choice")

print_menu()
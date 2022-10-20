# Inporting dependencies
import pickle

# Startup message
print("--- STUDENT RECORDS PROGRAM  ---")
print("-- N K Bagrodia Public School, Rohini - 110085 --\n")

fname = "students.dat" # fname stores the name of the file to be accessed


def addRec():
    """
        (function) addRec: () -> None

        The addRec() function can be used to add any number of records to the binary file. It takes roll number, name and marks of student repetitively (through a while loop) unless the user denies further inputs.
    """
    records = []

    with open(fname, "ab") as fptr:
        while True:
            rno = int(input("Enter roll number of student: "))
            name = input("Enter name of student: ")
            marks = int(input("Enter marks of student: "))

            record = {rno: [name, marks]}
            records.append(record)

            print("Do you wish to continue adding records? (y/n) ", end="")
            selection = input()
            
            if selection.strip().lower() in ['y', 'yes']:
                continue
            else:
                break

        pickle.dump(records, fptr)


def editRec():
    """
        (function) editRec: () -> None

        The editRec() function allows the user to edit the marks of any student. The function takes the target roll no. as input and finds the corresponding record in the table. If it is not able to find the roll no., it outputs a message. 
    """
    with open(fname, "rb") as fptr:
        tget = int(input("Enter roll no of student: "))
        records = pickle.load(fptr)
        for record in records:
            for rno in record:
                if rno == tget:
                    new_marks = int(input("Enter new marks of student: "))
                    record[rno][1] = new_marks
                    break
            print("ERROR: Could not find the associated record.")
            
    with open(fname, "wb") as fptr:
        pickle.dump(records, fptr)


def dispRec():
    """
        (function) dispRec: () -> None

        dispRec() function simply displays all the records in the binary file in a somewhat tabular format.
        The format of the output is - rno, name, marks.
    """
    with open(fname, "rb") as fptr:
        records = pickle.load(fptr)
        print(fname, "has the following content: ")
        for record in records:
            for rno in record:
                print(f"{rno}, {record[rno][0]}, {record[rno][1]}")


def main():
    print("MAIN MENU\n")
    print("\t-> To add records, enter 0 when prompted.")
    print("\t-> To edit records, enter 1 when prompted.")
    print("\t-> To display records, enter 2 when prompted.")
    print("\t-> To exit the program, enter 3 when prompted.\n")

    while True:
        print("Make a selection: ", end="")
        selection = int(input())
        print()

        if selection == 0:
            addRec() # calling statement for addRec() defined on line 11
        elif selection == 1:
            editRec() # calling statement for editRec() defined on line 39
        elif selection == 2:
            dispRec() # calling statement for dispRec() defined on line 60
        elif selection == 3:
            break
        else:
            print("ERROR: Invalid selection. Try again.")
            print()
            continue
        print()

        while True:
            print("Do you wish to return to the MAIN MENU? (y/n) ", end="")
            selection = input()

            if selection.strip().lower() in ['y', 'yes']:
                print()
                main()
            elif selection.strip().lower() in ['n', 'no']:
                return
            else:
                print("ERROR: Invalid selection. Try again.")
                print()   
    

if __name__ == "__main__": # Calling statement for main() function
    main()
import random


def menu():
    print("""Press the following numbers to interact :-
1. Admission of a child(ren).
2. Check the information of a child.
3. Change Fixed fees.
4. Get the grade of the student.
5. Change the information.""")
    choice = int(input("Enter the number: "))
    if choice == 1:
        admission()
        return "Admission"
    elif choice == 2:
        search_query()
        return "Information"
    elif choice == 3:
        change_fees()
        return "Change fixed fees"
    elif choice == 4:
        get_grades()
        return "Get grades"
    elif choice == 5:
        change_info()
        return "Change information"

fees = None


def change_fees():
    global fees
    new_fees = int(input("Enter a new fixed fees: "))
    fees = new_fees
    true = False
    ques = input("Do You Want to check the due fees\nof any student: ").upper()
    if ques == "Y":
        file = open("Data.txt")
        roll_no = input("Enter the roll no of the student: ")
        for i in file.readlines():
            fiel = i.split("    ")
            if fiel[3] == roll_no:
                true = True
                fees_paid = int(fiel[5])
                if fees_paid > fees:
                    print(f"{fiel[0]} paid {fees_paid-fees} more")
                elif fees_paid == fees:
                    print(f"{fiel[0]} have paid exactly the fees")
                elif fees_paid < fees:
                    print(f"{fiel[0]} need to pay {fees - fees_paid} more.")
        if not true:
            print("There no student with roll no {}".format(roll_no))


def get_grades():
    query = input("Enter the roll no of the student\nYou want to see grades: ")
    true = False
    with open("Data.txt") as data:
        lines = data.readlines()
        for i in lines:
            each = i.split("    ")
            if query == each[3]:
                print(f"{each[0]} got \"{each[4]}\"")
                true = True
        if not true:
            print(f"Nobody's roll no is {query}")


def change_info():
    print("""1. To change the name of the student.
2. To change the class of the student.
3. To change the age of the student.
4. To change the paid fees.
5. To change the marks.""")
    enter = int(input("Enter: "))
    if enter == 1:
        change_name()
    elif enter == 2:
        change_class()
    elif enter == 3:
        change_age()
    elif enter == 4:
        change_paid_fees()
    elif enter == 5:
        change_marks()


def change_name():

    num = 0
    enter = input("Enter the roll no of the student: ")
    with open("Data.txt", "r") as file:
        read = file.read()
    with open("Data.txt", "w") as files:
        read_lines = read.split("\n")
        for i in read_lines:
            words = i.split("    ")
            if words[3] == enter:
                index = read_lines.index('    '.join(words))
                new_name = input(f"Enter the new name of {words[num]}: ")
                words[num] = new_name
                words = '    '.join(words)
                break
        read_lines[index] = words
        read_lines = "\n".join(read_lines)
        files.write(read_lines)



def change_age():

    num = 1
    enter = input("Enter the roll no of the student: ")
    with open("Data.txt", "r") as file:
        read = file.read()
    with open("Data.txt", "w") as files:
        read_lines = read.split("\n")
        for i in read_lines:
            words = i.split("    ")
            if words[3] == enter:
                index = read_lines.index('    '.join(words))
                new_age = input(f"Enter the new age of {words[0]}: ")
                words[num] = new_age
                words = '    '.join(words)
                break
        read_lines[index] = words
        read_lines = "\n".join(read_lines)
        files.write(read_lines)

def change_class():

    num = 2
    enter = input("Enter the roll no of the student: ")
    with open("Data.txt", "r") as file:
        read = file.read()
    with open("Data.txt", "w") as files:
        read_lines = read.split("\n")
        for i in read_lines:
            words = i.split("    ")
            if words[3] == enter:
                index = read_lines.index('    '.join(words))
                new_name = input(f"Enter the new class of {words[0]}: ")
                words[num] = new_name
                words = '    '.join(words)
                break
        read_lines[index] = words
        read_lines = "\n".join(read_lines)
        files.write(read_lines)

def change_marks():
    num = 4
    enter = input("Enter the roll no of the student: ")
    with open("Data.txt", "r") as file:
        read = file.read()
    with open("Data.txt", "w") as files:
        read_lines = read.split("\n")
        for i in read_lines:
            words = i.split("    ")
            if words[3] == enter:
                index = read_lines.index('    '.join(words))
                new_name = input(f"Enter the new marks of {words[0]}: ")
                new_name = mark(new_name)
                words[num] = new_name
                words = '    '.join(words)
                break
        read_lines[index] = words
        read_lines = "\n".join(read_lines)
        files.write(read_lines)

def change_paid_fees():
    num = 5
    enter = input("Enter the roll no of the student: ")
    with open("Data.txt", "r") as file:
        read = file.read()
    with open("Data.txt", "w") as files:
        read_lines = read.split("\n")
        for i in read_lines:
            words = i.split("    ")
            if words[3] == enter:
                index = read_lines.index('    '.join(words))
                new_name = input(f"Enter the new fees of {words[0]}: ")
                words[num] = new_name
                words = '    '.join(words)
                break
        read_lines[index] = words
        read_lines = "\n".join(read_lines)
        files.write(read_lines)

roll_nos = None


def roll_no_generator():
    with open("Roll No.txt", 'r') as file:
        global roll_nos
        roll_nos = int(''.join(file.readlines()))
        roll_nos += random.randint(1, 100)
    with open("Roll No.txt", 'w') as files:
        files.write(str(roll_nos))
        return roll_nos


def mark(n):
    n = int(n)
    if 0 <= n < 49:
        return "F"
    elif 50 <= n <= 54:
        return "D"
    elif 55 <= n <= 59:
        return "C-"
    elif 60 <= n <= 64:
        return "C+"
    elif 65 <= n <= 69:
        return "B-"
    elif 70 <= n <= 74:
        return "B+"
    elif 75 <= n <= 79:
        return "A-"
    elif 80 <= n <= 100:
        return "A+"


def search_query():
    query = input("Enter the roll no: ")
    question = False
    try:
        with open("Data.txt", 'r') as file:
            file_data = file.readlines()
            for i in file_data:
                split = i.split("    ")

                if str(query) == split[3]:
                    print(f'''\nThe Name of the student is {split[0]} 
and she/he is in class {split[2]}''')
                    question = True
            if not question:
                print(f"There is no such roll no with {query}.")
    except IndexError:
        print("Please remove the blank line in the data file.\nand restart the program.")


def admission():
    global fees

    for _ in range(int(input("How many students do you want to admit: "))):

        name = input("Name of student: ")
        name = name.strip()
        age = input("Age of the student: ")

        class_of_student = input("Enter The Class and section: ")
        marks = input("Enter the marks of the "+name+": ")
        fees = 5000
        fees_paid = int(input("Enter the fees paid: "))
        due_fees = fees - fees_paid
        if fees < fees_paid:
            print("You have paid more than enough.")
        elif fees == fees_paid:
            print("You paid exactly the amount of fees.")
        else:
            print(f'{name} needs to pay {due_fees}')
        marks = mark(marks)

        roll_no = roll_no_generator()
        with open("Data.txt", 'a') as data:
            data.write('\n')
            data.write('    '.join([name, age, class_of_student, str(roll_no), marks, str(fees_paid)]))
            print("\nThe Data has been saved to the system.\n")

            print("The Roll no. of {} is {}".format(name, roll_no))


menu()

import os


def add_student(name, surname, group):
    file = open("Student_list.txt", "a", encoding="utf8")
    file.write(f"{name};{surname};{group}\n")
    file.close()


def show_students():
    if os.path.isfile("Student_list.txt") == False:
        print("add a student to the list first")
    else:

        file = open("Student_list.txt", "r", encoding="utf8")
        for i in file:
            x = i.split(";")
            print(f"name: {x[0]}, surname: {x[1]}, group: {x[2]}", end="")
            if len(x) >= 4:
                aid = 0
                sum = 0
                o = x[3].split(" ")
                for w in range(len(o) - 1):
                    sum += int(o[w])
                    aid += 1
                average = sum / aid
                print(
                    f", average: {round(average,2)}"
                )  # w will never be 0 due to \n sign

            else:
                print("")

        file.close()


def delete_student(surname):
    aid = []
    file_r = open("Student_list.txt", "r", encoding="utf8")
    for i in file_r:
        x = i.split(";")
        if x[1] != surname:
            aid.append(i)
    file_r.close()

    file_w = open("Student_list.txt", "w", encoding="utf8")
    file_w.writelines(aid)
    file_w.close()


def change_details(surname, new_name, new_surname):
    aid = []
    file_r = open("Student_list.txt", "r", encoding="utf8")
    for i in file_r:
        x = i.split(";")
        if x[1] == surname:
            aid.append(f"{new_name};{new_surname};{x[2]}")
        else:
            aid.append(i)
    file_r.close()

    file_w = open("Student_list.txt", "w", encoding="utf8")
    file_w.writelines(aid)
    file_w.close()


def check(surname):
    if os.path.isfile("Student_list.txt") == False:
        print("add a student to the list first")
        return 2
    else:
        file = open("Student_list.txt", "r", encoding="utf8")
        for i in file:
            x = i.split(";")
            if x[1] == surname:
                file.close()
                return 1


def grade(name, surname, grades):
    students = []
    file_r = open("Student_list.txt", "r", encoding="utf8")
    for i, y in enumerate(file_r):
        x = y.split(";")
        if x[0] != name or x[1] != surname:
            students.append(y)
        else:

            students.append("")
            for s, u in enumerate(x):
                if s == 3:
                    change_details = u.replace("\n", "")
                    students[i] = f"{students[i]}{change_details}"
                else:
                    students[i] = f"{students[i]}{u.strip()};"
            for w in grades:
                students[i] = f"{students[i]}{w} "
            students[i] = f"{students[i]}\n"
    file_r.close()

    file_w = open("Student_list.txt", "w", encoding="utf8")
    file_w.writelines(students)
    file_w.close()


while True:

    menu = input(
        "1-add student, 2-show current students, 3-delete a student, 4-change student's details, 5-add_student's grades, 6-end: "
    )

    if menu == "1":
        name = input("name: ")
        surname = input("surname: ")
        group = input("group: ")
        add_student(name, surname, group)

    elif menu == "2":
        show_students()

    elif menu == "3":
        surname = input("surname of the student pending deletion: ")
        checking = check(surname)
        if checking == 1:
            delete_student(surname)
        elif checking != 2:
            print("Surname not found")

    elif menu == "4":
        surname = input("surname of the student pending details change: ")
        checking = check(surname)
        if checking == 1:
            new_name = input("New name: ")
            new_surname = input("New surname: ")
            change_details(surname, new_name, new_surname)
        elif checking != 2:
            print("Surname not found")

    elif menu == "5":
        surname = input("surname: ")
        checking = check(surname)
        if checking == 1:
            name = input("name: ")
            grades_list = []
            while True:
                grades = int(input("Add student's grades ending with 0: "))
                if grades != 0:
                    grades_list.append(grades)
                else:
                    break
            grade(name, surname, grades_list)

        elif checking != 2:
            print("Surname not found")

    elif menu == "6":
        break

import sqlite3

try:
    conn = sqlite3.connect(
        'employees.db'
    )
    c = conn.cursor()
    print("connection successful!")
except:
    raise ConnectionError('could not connect to the database')


def add_employee(name, surname, salary):
    sql = f"INSERT INTO employees(name,surname,salary) VALUES ('{name}', '{surname}',{salary})"
    c.execute(sql)

    dec = input("add input to the database? T/N: ").upper()

    if dec == "T":
        conn.commit()
        print("details successfully added")

    else:
        conn.rollback()
        print("cancelled")


def show():
    sql = "SELECT * FROM employees"
    c.execute(sql)
    data = c.fetchall()
    for i in data:
        print(f"ID: {i[0]}, name: {i[1]}, surname: {i[2]}, salary {i[3]}")


def delete_employee(surname):
    sql = f"SELECT * FROM employees WHERE surname = '{surname}'"
    c.execute(sql)
    data = c.fetchall()
    if not data:
        print("employee not found")
    else:
        sql = f"DELETE FROM employees WHERE employeeid = '{data[0][0]}'"
        c.execute(sql)

        dec = input("delete employee? T/N: ").upper()

        if dec == "T":
            conn.commit()
            print(f"deleted {surname} from {data[0][0]}")

        else:
            conn.rollback()
            print("cancelled")


def modify(surname, value):

    sql = f"SELECT * FROM employees WHERE surname = '{surname}'"
    c.execute(sql)
    data = c.fetchall()
    if not data:
        print("employee not found")
    else:
        for i in value:
            sql = f"UPDATE employees SET {i[0]} = '{i[1]}' WHERE employeeid = '{data[0][0]}'"
            c.execute(sql)

        dec = input("modify database? T/N: ").upper()

        if dec == "T":
            conn.commit()
            print(f"modified")

        else:
            conn.rollback()
            print("cancelled")


def search(searched_value):
    sql = f"SELECT * FROM employees WHERE surname LIKE '%{searched_value}%' OR name LIKE '%{searched_value}%'"
    c.execute(sql)
    data = c.fetchall()
    for i in data:
        print(f"ID: {i[0]}, name: {i[1]}, surname: {i[2]}, salary {i[3]}")


while True:

    menu = input(
        "1-add employee, 2-show, 3-delete employee, 4-modify, 5-search, 6-quit: "
    )

    if menu == "1":
        name = input("name: ")
        surname = input("surname: ")
        salary = int(input("salary: "))
        add_employee(name, surname, salary)

    elif menu == "2":
        show()

    elif menu == "3":
        surname = input("surname: ")
        delete_employee(surname)

    elif menu == "4":
        value = []
        old_surname = input("employee's surname:")
        change = int(input("Value to modify? 1-all, 2-name, 3-surname, 4- salary: "))
        if change == 1:
            name = input("new name: ")
            new_surname = input("new surname: ")
            salary = int(input("new salary: "))

            value.append(["name", name])
            value.append(["salary", salary])
            value.append(["surname", new_surname])
            modify(old_surname, value)

        elif change == 2:
            name = input("new name: ")
            value.append(["name", name])
            modify(old_surname, value)
        elif change == 3:
            new_surname = input("new surname: ")
            value.append(["surname", new_surname])
            modify(old_surname, value)
        elif change == 4:
            salary = input("new salary: ")
            value.append(["salary", salary])
            modify(old_surname, value)

    elif menu == "5":
        searched_value = input("searched_value phrase: ")
        search(searched_value)
    elif menu == "6":
        print("quitting")
        conn.close()
        break
    else:
        print("Unknown option")

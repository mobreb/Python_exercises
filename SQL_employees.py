import sqlite3

# Connecting to sqlite, raising an error if unsuccessful

try:
    conn = sqlite3.connect("employees.db")
    c = conn.cursor()
    print("connection successful!")
except:
    raise ConnectionError("could not connect to the database")


def add_employee(name: str, surname: str, salary: int) -> None:
    """Add an employee to DB by providing name, surname and salary Confirm before committing."""
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
    """Returns all records from DB."""
    sql = "SELECT * FROM employees"
    c.execute(sql)
    data = c.fetchall()
    for i in data:
        print(f"ID: {i[0]}, name: {i[1]}, surname: {i[2]}, salary {i[3]}")


def delete_employee(employee_surname: str, employee_id: str) -> None:
    """Delete employee from DB by searching for employee id. Print error if employee not found."""
    sql = f"DELETE FROM employees WHERE employeeid = '{employee_id}'"
    c.execute(sql)

    dec = input("delete employee? T/N: ").upper()

    if dec == "T":
        conn.commit()
        print(f"deleted {employee_surname} from {employee_id}")

    else:
        conn.rollback()
        print("cancelled")


def modify(employee_id: str, value: list) -> None:
    """Amend employee information. Takes in employee_id and a list containing column and value to be modified."""
    for i in value:
        sql = (
            f"UPDATE employees SET {i[0]} = '{i[1]}' WHERE employeeid = '{employee_id}'"
        )
        c.execute(sql)

    dec = input("modify database? T/N: ").upper()

    if dec == "T":
        conn.commit()
        print(f"modified")

    else:
        conn.rollback()
        print("cancelled")


def search(searched_value: str) -> None:
    """Input: partial/full name or surname as a string."""
    sql = f"SELECT * FROM employees WHERE surname LIKE '%{searched_value}%' OR name LIKE '%{searched_value}%'"
    c.execute(sql)
    data = c.fetchall()
    if data:
        for i in data:
            print(f"ID: {i[0]}, name: {i[1]}, surname: {i[2]}, salary {i[3]}")
    else:
        raise ValueError("Data not found")


def check_surname(surname: str) -> str:
    """Ensure the employee is a member of the DB. Input surname, return employee id"""
    sql = f"SELECT * FROM employees WHERE surname = '{surname}'"
    c.execute(sql)
    data = c.fetchall()
    if not data:
        raise ValueError("Employee not found")
    else:
        return f"{data[0][0]}"


def main():
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
            delete_employee(
                employee_surname=surname, employee_id=check_surname(surname)
            )

        # Modify employees information, option to choose which value to modify
        elif menu == "4":
            value = []
            old_surname = input("employee's surname:")
            employee_id = check_surname(old_surname)
            change = int(
                input("Value to modify? 1-all, 2-name, 3-surname, 4- salary: ")
            )
            if change == 1:
                name = input("new name: ")
                new_surname = input("new surname: ")
                salary = int(input("new salary: "))

                value.append(["name", name])
                value.append(["salary", salary])
                value.append(["surname", new_surname])
                modify(employee_id, value)

            elif change == 2:
                name = input("new name: ")
                value.append(["name", name])
                modify(employee_id, value)
            elif change == 3:
                new_surname = input("new surname: ")
                value.append(["surname", new_surname])
                modify(employee_id, value)
            elif change == 4:
                salary = input("new salary: ")
                value.append(["salary", salary])
                modify(employee_id, value)

        elif menu == "5":
            searched_value = input("searched_value phrase: ")
            search(searched_value)

        # Disconnect from DB, close program
        elif menu == "6":
            print("quitting")
            conn.close()
            break
        # Pass an error if option out of the list is not chosen
        else:
            print("Unknown option")


if __name__ == "__main__":
    main()

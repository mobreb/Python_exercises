import pickle


class Employee:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.employment = []

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @name.setter
    def name(self, name):
        self.__name = name

    @surname.setter
    def surname(self, surname):
        self.__surname = surname


class Company:
    def __init__(self, label):
        self.__label = label
        self.employee_list = []

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label):
        self.__label = label


class CompanyController:
    def __init__(self):
        self.companies_list = []
        self.employees = []

    def add_company(self, label):
        company = Company(label)
        self.companies_list.append(company)

    def delete_company(self, label):
        for i in self.companies_list:
            if i.label == label:
                if len(i.employee_list) == 0:
                    self.companies_list.remove(i)
                else:
                    print("Cannot delete due to existing employees")
                break

    def display_companies(self):
        for i in self.companies_list:
            print(i.label)

    def add_employee(self, name, surname):
        employee = Employee(name, surname)
        self.employees.append(employee)

    def delete_employee(self, surname):
        for i in self.employees:
            if i.surname == surname:
                if len(i.employment) == 0:
                    self.employees.remove(i)
                else:
                    print("Employee assigned to a company")

    def show_employees(self):
        for i in self.employees:
            print(f"{i.name} {i.surname}")

    def assign_company(self, surname, label):
        for i in self.employees:
            if i.surname == surname:
                i.employment.append(label)
                for j in self.companies_list:
                    if j.label == label:
                        j.employee_list.append(i)
                        break
                break

    def contract_termination(self, surname, label):
        for i in self.employees:
            if i.surname == surname:
                i.employment.remove(label)
                for j in self.companies_list:
                    if j.label == label:
                        j.employee_list.remove(i)
                        break
                break

    def display_employment(self, surname):
        for i in self.employees:
            if i.surname == surname:
                for j in i.employment:
                    print(j)

    def save(self):
        saved_file = [self.companies_list, self.employees]
        file = open("companies_list.dat", "wb")
        pickle.dump(saved_file, file)
        file.close()


class Application(CompanyController):
    def __init__(self):
        super().__init__()
        try:
            file = open("companies_list.dat", "rb")
            read_file = pickle.load(file)
            self.companies_list = read_file[0]
            self.employees = read_file[1]
            file.close()

        except:
            file = open("companies_list.dat", "wb")
            pickle.dump([], file)
            file.close()

        self.menu()

    def menu(self):
        while True:
            menu = int(
                input("Manage: 1 - Company, 2 - Employee, 3 - Employment, 0 - Exit: ")
            )
            if menu == 1:
                while True:
                    menu_company = int(
                        input(
                            "1 - Add a company, 2 - Delete a company, 3 - Display a company, 0 - Exit company's module: "
                        )
                    )
                    if menu_company == 1:
                        label = input("Company's name: ")
                        self.add_company(label)
                    elif menu_company == 2:
                        label = input("Company to delete")
                        self.delete_company(label)
                    elif menu_company == 3:
                        self.display_companies()
                    elif menu_company == 0:
                        self.save()
                        break
                    else:
                        print("Please input a correct value ranging from 0 to 3")
            elif menu == 2:
                while True:
                    menu_employee = int(
                        input(
                            "1 - Add employee, 2 - Remove employee, 3 - Show employees, 0 - Exit employee module "
                        )
                    )
                    if menu_employee == 1:
                        name = input("name: ")
                        surname = input("surname: ")
                        self.add_employee(name, surname)
                    elif menu_employee == 2:
                        surname = input("Employee's surname for company withdrawal: ")
                        self.delete_employee(surname)
                    elif menu_employee == 3:
                        self.show_employees()
                    elif menu_employee == 0:
                        self.save()
                        break
                    else:
                        print("Please input a correct value ranging from 0 to 3")
            elif menu == 3:
                while True:
                    menu_employment = int(
                        input(
                            "1 - Assign a company to employee, 2 - Remove a company from employee, 3 - Show employment, 0 - Exit employment module: "
                        )
                    )
                    if menu_employment == 1:
                        surname = input("Employee's surname: ")
                        label = input("Assign a company: ")
                        self.assign_company(surname, label)

                    elif menu_employment == 2:
                        surname = input("Employee's surname: ")
                        label = input("Company's name: ")
                        self.contract_termination(surname, label)
                    elif menu_employment == 3:
                        surname = input("Employee's surname: ")
                        self.display_employment(surname)
                    elif menu_employment == 0:
                        self.save()
                        break
                    else:
                        print("Please input a correct value ranging from 0 to 3")
            elif menu == 0:
                break
            else:
                print("Please input a correct value ranging from 0 to 3")


application = Application()

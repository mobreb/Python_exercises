from dataclasses import dataclass, field
import pickle
from typing import Any


@dataclass(frozen=True)
class Employee:
    """Class for keeping track of employee information"""

    name: str
    surname: str
    employment: list[Any] = field(default_factory=list)


@dataclass(frozen=True)
class Company:
    """CLass for keeping track of company information and employees assigned"""

    company_name: str
    employee_list: list[str] = field(default_factory=list)


@dataclass
class CompanyController:
    companies_list: list[Any] = field(default_factory=list)
    employees: list[Any] = field(default_factory=list)

    def add_company(self, company_name: str) -> None:
        aid = 0
        for c in self.companies_list:
            if c.__dict__["company_name"] == company_name:
                aid = 1
                break
        if aid == 0:
            company = Company(company_name)
            self.companies_list.append(company)
        else:
            raise ValueError("Company name already taken")

    def delete_company(self, company_name: str) -> None:
        for i in self.companies_list:
            if i.company_name == company_name:
                if not i.employee_list:
                    self.companies_list.remove(i)
                else:
                    raise ValueError("Cannot delete due to existing employees")
                break

    def display_companies(self) -> None:
        for i in self.companies_list:
            print(i.company_name)

    def add_employee(self, name: str, surname: str) -> None:
        employee = Employee(name, surname)
        self.employees.append(employee)

    def delete_employee(self, surname: str) -> None:
        for i in self.employees:
            if i.surname == surname:
                if not i.employment:
                    self.employees.remove(i)
                else:
                    print("Employee assigned to a company")

    def show_employees(self) -> None:
        for i in self.employees:
            print(f"{i.name} {i.surname}")

    def assign_company(self, surname: str, company_name: str) -> None:
        for i in self.employees:
            if i.surname == surname:
                i.employment.append(company_name)
                for j in self.companies_list:
                    if j.company_name == company_name:
                        j.employee_list.append(i)
                        break
                break

    def contract_termination(self, surname: str, company_name: str) -> None:
        for i in self.employees:
            if i.surname == surname:
                i.employment.remove(company_name)
                for j in self.companies_list:
                    if j.company_name == company_name:
                        j.employee_list.remove(i)
                        break
                break

    def display_employment(self, surname: str) -> None:
        for i in self.employees:
            if i.surname == surname:
                for j in i.employment:
                    print(j)

    def save(self) -> None:
        saved_file = [self.companies_list, self.employees]
        file = open("companies_list.dat", "wb")
        pickle.dump(saved_file, file)
        file.close()


class Main(CompanyController):
    def __init__(self):
        super().__init__()
        try:
            with open("companies_list.dat", "rb") as file:
                read_file = pickle.load(file)
                self.companies_list, self.employees = read_file
        except:
            with open("companies_list.dat", "wb") as file:
                pickle.dump([], file)

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
                        company_name = input("Company's name: ")
                        self.add_company(company_name=company_name)
                    elif menu_company == 2:
                        company_name = input("Company to delete: ")
                        self.delete_company(company_name=company_name)
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


if __name__ == "__main__":
    application = Main()
    application.menu()

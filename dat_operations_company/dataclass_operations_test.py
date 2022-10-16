from typing import Any

import dataclass_operations
import unittest
import pytest


class TestCompanyController(unittest.TestCase):
    application = dataclass_operations.Main()

    def company_name_search(self):
        test_list = []
        for company in self.application.companies_list:
            test_list.append(company.__dict__["company_name"])
        return test_list

    def employee_search(self):
        test_list = []
        for employee in self.application.employees:
            test_list.append(employee.__dict__["surname"])
        return test_list

    def test_add_company(self):
        self.application.add_company(company_name="test company")
        test_list = self.company_name_search()
        self.assertIn("test company", test_list, "Company not added to the list")
        with pytest.raises(ValueError):
            self.application.add_company(company_name="test company")

    def test_delete_company(self):
        self.application.delete_company(company_name="test company")
        test_list = self.company_name_search()
        self.assertNotIn("test company", test_list, "THe company has not been deleted")

    def test_add_employee(self):
        self.application.add_employee("test name", "test surname")
        test_list = self.employee_search()
        self.assertIn("test surname", test_list, "Employee not added to the list")

    def test_employee_assignment(self):
        employee_list_holder: list[Any] = []
        company_name_holder: list[str] = []
        self.application.add_company(company_name="testing assignment company")
        self.application.assign_company(
            surname="testing assignment employee false",
            company_name="testing assignment company",
        )
        self.application.add_employee(
            name="test", surname="testing assignment employee"
        )
        self.application.assign_company(
            surname="testing assignment employee",
            company_name="testing assignment company",
        )
        for company in self.application.companies_list:
            if company.company_name == "testing assignment company":
                for employee in company.employee_list:
                    employee_list_holder.append(employee.__dict__["surname"])
                    if employee.surname == "testing assignment employee":
                        company_name_holder = employee.employment
                break

        self.assertIn(
            "testing assignment employee",
            employee_list_holder,
            "Employee not found in companies employment list",
        )
        self.assertNotIn("testing assignment employee false", employee_list_holder)
        self.assertIn(
            "testing assignment company",
            company_name_holder,
            "Employment not assigned to employee",
        )

    def test_delete_company_with_employees(self):
        self.application.add_company(
            company_name="testing deleting company with employees"
        )
        self.application.add_employee(name="test", surname="testing employee to delete")
        self.application.assign_company(
            surname="testing employee to delete",
            company_name="testing deleting company with employees",
        )
        with pytest.raises(ValueError):
            self.application.delete_company("testing deleting company with employees")

    def test_contract_termination(self):
        employee_list_holder: list[Any] = []
        company_name_holder: list[str] = []
        self.application.add_company(company_name="testing contract termination")
        self.application.add_employee(
            name="test", surname="testing employee to terminate contract"
        )
        self.application.assign_company(
            surname="testing employee to terminate contract",
            company_name="testing contract termination",
        )
        self.application.contract_termination(
            surname="testing employee to terminate contract",
            company_name="testing contract termination",
        )
        for company in self.application.companies_list:
            if company.company_name == "testing contract termination":
                for employee in company.employee_list:
                    employee_list_holder.append(employee.__dict__["surname"])
                    if employee.surname == "testing employee to terminate contract":
                        company_name_holder = employee.employment
        self.assertNotIn(
            "testing employee to terminate contract",
            company_name_holder,
            "Company not removed from employment list upon contract termination",
        )
        self.assertNotIn(
            "testing contract termination",
            company_name_holder,
            "Employee not removed from employees list upon contract termination",
        )

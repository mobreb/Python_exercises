class Patient:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
        self.sickness_list = []

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


class Clinic:
    def __init__(self, designation, city):
        self.__designation = designation
        self.__city = city
        self.patients_list = []

    @property
    def designation(self):
        return self.__designation

    @property
    def city(self):
        return self.__city

    @designation.setter
    def designation(self, designation):
        self.__designation = designation

    @city.setter
    def city(self, city):
        self.__city = city


class Menu:
    def __init__(self):
        self.clinic_list = []
        self.start()

    def add_clinic(self, designation, city):
        clinic = Clinic(designation, city)
        self.clinic_list.append(clinic)

    def remove_clinic(self, clinic_designation):
        for i in self.clinic_list:
            if i.designation == clinic_designation:
                self.clinic_list.remove(i)
                return 1
        print("Clinic not in the database")

    def check_designation(self, designation):
        for i in self.clinic_list:
            if i.designation == designation:
                return 1
        print("Clinic not in the database")

    def add_patient(self, name, surname, designation):
        patient = Patient(name, surname)
        for i in self.clinic_list:
            if i.designation == designation:
                i.patients_list.append(patient)

    def display_clinic(self):
        for i in self.clinic_list:
            print(i.designation)

    def display_patients(self, designation):
        for i in self.clinic_list:
            if i.designation == designation:
                for j in i.patients_list:
                    print(j.name, j.surname)

    def check_surname(self, surname, designation):
        for i in self.clinic_list:
            if i.designation == designation:
                for j in i.patients_list:
                    if j.surname == surname:
                        return 1
        print("Patient not assigned to the clinic")

    def add_sickness(self, surname, designation, sickness):
        for i in self.clinic_list:
            if i.designation == designation:
                for j in i.patients_list:
                    if j.surname == surname:
                        j.sickness_list.append(sickness)

    def display_sicknesses(self, surname, designation):
        for i in self.clinic_list:
            if i.designation == designation:
                for j in i.patients_list:
                    if j.surname == surname:
                        for h in j.sickness_list:
                            print(h)

    def start(self):
        while True:
            menu = int(input("Menu: 1-Clinic, 2-Patient, 3-Quit: "))
            if menu == 1:

                option = int(
                    input(
                        "Clinic menu: 1-Add a clinic, 2-Remove clinic, 3-Add a patient to the clinic, 4-Clinic list, 5-Clinic's patients list, 6-Return : "
                    )
                )
                if option == 1:
                    designation = input("Clinic's name")
                    city = input("City: ")
                    self.add_clinic(designation, city)

                elif option == 2:
                    designation = input("Clinic to be removed: ")
                    self.remove_clinic(designation)

                elif option == 3:
                    designation = input("Clinic's name: ")
                    if self.check_designation(designation) == 1:
                        name = input("Patient's name: ")
                        surname = input("Patient's surname: ")
                        self.add_patient(name, surname, designation)

                elif option == 4:
                    self.display_clinic()
                elif option == 5:
                    designation = input("Clinic's name: ")
                    if self.check_designation(designation) == 1:
                        self.display_patients(designation)
                elif option == 6:
                    pass
                else:
                    print("Please choose out of existing options: ")
            elif menu == 2:
                designation = input("Clinic's name: ")
                if self.check_designation(designation) == 1:
                    surname = input("Patient's surname: ")
                    if self.check_surname(surname, designation) == 1:
                        option = int(
                            input("Patient's menu: 1-Add sickness, 2-Sickness list: ")
                        )
                        if option == 1:
                            sickness = input("Sickness: ")
                            self.add_sickness(surname, designation, sickness)
                        elif option == 2:
                            self.display_sicknesses(surname, designation)
                        else:
                            print(
                                "Please choose out of existing options in patient's menu: "
                            )
            elif menu == 3:
                break
            else:
                print("Please choose out of existing options in main menu: ")


menu = Menu()

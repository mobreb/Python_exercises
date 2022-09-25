class Person:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

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


class Student(Person):
    def __init__(self, name, surname, email):
        super().__init__(name, surname)
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email


class Trainer(Person):
    def __init__(self, name, surname, specialization):
        super().__init__(name, surname)
        self.__specialization = specialization

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, specialization):
        self.__specialization = specialization


class Course:
    def __init__(self, label, city, timeslot):
        self.__label = label
        self.__place = city
        self.__timeslot = timeslot
        self.trainer_list = []
        self.student_list = []

    @property
    def label(self):
        return self.__label

    @property
    def place(self):
        return self.__place

    @property
    def timeslot(self):
        return self.__timeslot

    @label.setter
    def label(self, label):
        self.__label = label

    @timeslot.setter
    def timeslot(self, timeslot):
        self.__timeslot = timeslot

    @place.setter
    def place(self, city):
        self.__place = city


class ControllerCourse:
    def __init__(self):
        self.course_dict = {}

    def add_course(self, label, place, timeslot):
        course = Course(label, place, timeslot)
        self.course_dict[label] = course

    def add_trainer(self, name, surname, specialization, label):
        trainer = Trainer(name, surname, specialization)
        self.course_dict[label].trainer_list.append(trainer)

    def add_student(self, name, surname, email, label):
        student = Student(name, surname, email)
        self.course_dict[label].student_list.append(student)

    def check_students(self, label):
        if len(self.course_dict[label].student_list) < 5:
            return 1
        else:
            print("Course is already full - 5 participants limit")
            return 2

    def delete_trainer(self, surname, label):
        for i in self.course_dict[label].trainer_list:
            if i.surname == surname:
                self.course_dict[label].trainer_list.remove(i)
                print(f"Trainer {i.surname} was removed from the course")
                break

    def delete_student(self, surname, label):
        for i in self.course_dict[label].student_list:
            if i.surname == surname:
                self.course_dict[label].student_list.remove(i)
                print(f"Student {i.surname} was removed")

    def delete_course(self, course):
        if len(self.course_dict[course].student_list) == 0:
            self.course_dict.pop(course)
            print(f"Course {course} was deleted")
        else:
            print(
                "There are active student accounts under the course, unable to delete."
            )

    def check_surname(self, surname, person, label):
        if person == "trainer":
            if len(self.course_dict[label].trainer_list) == 0:
                print("Lack of trainers assigned to the course")
                return 2

            else:
                for i in self.course_dict[label].trainer_list:
                    if i.surname == surname:
                        return 1

        elif person == "student":
            if len(self.course_dict[label].student_list) == 0:
                print("Lack of students assigned to the course")
                return 2
            else:
                for i in self.course_dict[label].student_list:
                    if i.surname == surname:
                        return 1

        print("Surname not found")

    def modify_student(self, new_name, new_surname, new_email, old_surname, label):
        for i in self.course_dict[label].student_list:
            if i.surname == old_surname:
                i.name = new_name
                i.surname = new_surname
                i.email = new_email
                break

    def modify_course(self, new_label, city, new_timeslot, course_label):
        self.course_dict[course_label].label = new_label
        self.course_dict[course_label].place = city
        self.course_dict[course_label].timeslot = new_timeslot

    def display_course(self):
        for course in self.course_dict:
            print(
                f"course {self.course_dict[course].label}, in city {self.course_dict[course].place} at {self.course_dict[course].timeslot}"
            )
            print("Taught by : ")
            for h in self.course_dict[course].trainer_list:
                print(f"{h.name} {h.surname}")
            print("Student list: ")
            for j in self.course_dict[course].student_list:
                print(f"{j.name} {j.surname}")
            print("")

    def check_label(self, label):
        if label in self.course_dict:
            return 1

        else:
            print("Course with a given label not found")
            return 2


class School(ControllerCourse):
    def __init__(self, label):
        super().__init__()
        self.__label = label
        self.menu()

    @property
    def label(self):
        return self.__label

    @label.setter
    def label(self, label):
        self.__label = label

    def menu(self):
        print(f"Welcome to {self.__label}")
        while True:
            menu = int(
                input(
                    "Menu: 1-Add course, 2-Add trainer to an existing course, 3-Add participant to an existing course, 4-Remove trainer, 5-Remove student, 6-Delete course, 7-Modify student's details, 8-Modify course details, 9-Display course, 0-Quit: "
                )
            )
            if menu == 1:
                label = input("Assign a label: ")
                place = input("Assign a city: ")
                timeslot = input("Assign a start date (dd-mm-yyyy): ")
                self.add_course(label, place, timeslot)

            elif menu == 2:
                label = input(
                    "Specify the course to which the trainer should be added: "
                )
                if self.check_label(label) == 1:
                    name = input("Trainer's name: ")
                    surname = input("Trainer's surname: ")
                    specialization = input("Trainer's specialization: ")
                    self.add_trainer(name, surname, specialization, label)

            elif menu == 3:
                label = input(
                    "Specify the course to which the student should be added: "
                )
                if self.check_label(label) == 1:
                    if self.check_students(label) == 1:
                        name = input("Student's name")
                        surname = input("Student's surname")
                        email = input("Student's email: ")
                        self.add_student(name, surname, email, label)

            elif menu == 4:
                label = input("Course from which the trainer should be removed from: ")
                if self.check_label(label) == 1:
                    surname = input("Surname of the trainer pending removal: ")
                    if self.check_surname(surname, "trainer", label) == 1:
                        self.delete_trainer(surname, label)

            elif menu == 5:
                label = input("Course from which the student should be removed from:")
                if self.check_label(label) == 1:
                    surname = input("Surname of the student pending removal: ")
                    if self.check_surname(surname, "student", label) == 1:
                        self.delete_student(surname, label)

            elif menu == 6:
                course = input("Course pending removal: ")
                self.delete_course(course)

            elif menu == 7:
                label = input("Specify the course: ")
                if self.check_label(label) == 1:
                    surname = input("Surname of student pending detail modification: ")
                    if self.check_surname(surname, "student", label) == 1:
                        new_name = input("New name: ")
                        new_surname = input("New surname: ")
                        new_email = input("New email: ")
                        self.modify_student(
                            new_name, new_surname, new_email, surname, label
                        )

            elif menu == 8:
                label = input("Specify the course: ")
                if self.check_label(label) == 1:
                    new_label = input("New label: ")
                    place = input("New city: ")
                    new_timeslot = input("New timeslot: ")
                    self.modify_course(new_label, place, new_timeslot, label)

            elif menu == 9:
                self.display_course()

            elif menu == 0:
                break
            else:
                print("Incorrect choice")


school = School(input("School name: "))

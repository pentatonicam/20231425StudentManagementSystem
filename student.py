class Student:

    def __init__(self, student_id, name, surname, age, department, gpa):
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.age = age
        self.department = department
        self.gpa = gpa

    def display_info(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name, self.surname)
        print("Age:", self.age)
        print("Department:", self.department)
        print("GPA:", self.gpa)

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

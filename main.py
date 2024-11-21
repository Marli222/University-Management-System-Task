import statistics

class Person:
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def set_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    
class Student(Person):
    def __init__(self,name, age, gender):
        super().__init__(name,age,gender)
        self.student_id = ''
        self.course = ''
        self.grades = []
        self.mentor = ''

    def set_student_details(self,student_id,course,mentor):
        self.student_id = student_id
        self.course = course
        self.mentor = mentor

    def add_grade(self,grade):
        (self.grades).append(grade)

    def calculate_average_grade(self):
        if self.grades == []:
            return 0
        else:
            return round((statistics.mean(self.grades)),2)
        
    def get_student_summary(self):
        return f"""
        Name: {self.name}
        Age: {self.age}
        Gender: {self.gender}
        Student Id: {self.student_id}
        Course: {self.course}
        Average Grade: {self.calculate_average_grade()}"""
    
    def get_mentor(self):
        if self.mentor == '':
            return "No mentor assigned."
        else:
            return self.mentor


class Professor(Person):
    def __init__(self,name, age, gender):
        super().__init__(name,age,gender)
        self.staff_id = ''
        self.department = ''
        self.salary = 0
        self.mentored_students = []
    
    def set_professor_details(self,staff_id, department, salary):
        self.staff_id = staff_id
        self.department = department
        self.salary = salary

    def give_feedback(self,student, feedback):
        return f"Feedback for {student.name}: {feedback}"
    
    def increase_salary(self,percentage):
        self.salary = (self.salary * percentage / 100) + self.salary

    def get_professor_summary(self):
        return f"""
        Name: {self.name}
        Age: {self.age}
        Gender: {self.gender}
        Staff Id: {self.staff_id}
        Department: {self.department}
        Salary: {self.salary}"""
    
    def mentor_student(self,student):
        (self.mentored_students).append(student.name)
        student.set_student_details(student.student_id, student.course, self.name)
        return f"Professor {self.name} is now mentoring Student {student.name} on {student.course}."
    
    def get_mentored_students(self):
        return self.mentored_students
    
class Admin(Person):
    def __init__(self,name, age, gender):
        super().__init__(name,age,gender)
        self.admin_id = ''
        self.office = ''
        self.years_of_service = 0
    
    def set_admin_details(self,admin_id, office, years_of_service):
        self.admin_id = admin_id
        self.office = office
        self.years_of_service = years_of_service

    def increment_service_years(self):
        self.years_of_service += 1

    def get_admin_summary(self):
        return f"""
        Name: {self.name}
        Age: {self.age}
        Gender: {self.gender}
        Staff Id: {self.admin_id}
        Years of Service: {self.years_of_service}
        Office: {self.office}"""
    
Armeen = Student("Armeen",21,"Female")
Marli = Student("Marli",20,"Female")
Prof1 = Professor("Dr. Smith", 45, "Male")
Prof1.set_professor_details('B1234','Science',100)
Prof2 = Professor("Dr. Alice", 32, "Female")
Admin1 = Admin("Vianna",67,"Female")

Armeen.add_grade(4)
Marli.add_grade(3)
Armeen.add_grade(7)
Marli.add_grade(2)
Armeen.add_grade(9)
Marli.add_grade(6)

print(Prof2.give_feedback(Marli,"Good job on the project!"))
print(Prof1.give_feedback(Armeen,"Good job on the project!"))
Prof1.increase_salary(10)
Admin1.increment_service_years()

print(Armeen.get_student_summary())
print(Marli.get_student_summary())
print(Prof1.get_professor_summary())
print(Prof2.get_professor_summary())
print(Admin1.get_admin_summary())

Prof2.mentor_student(Marli)
print(Armeen.get_mentor())
Prof2.mentor_student(Armeen)
print(Prof2.get_mentored_students())
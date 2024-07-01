class SchoolMember:
    """Initialize the class """

    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
        print("Initialized SchoolMember {}".format(self.name))

    def tell(self):
        print("Name: {}, Age: {}, School: {},".format(self.name, self.age, self.school), end=" ")


class Teacher(SchoolMember):
    def __init__(self, name, age, school, salary):
        SchoolMember.__init__(self, name, age, school)
        self.salary = salary
        print("Initialized Teacher {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Salary: {:d}".format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, school, marks):
        SchoolMember.__init__(self, name, age, school)
        self.marks = marks
        print("Initialized Student {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Marks: {:d}".format(self.marks))


student = Student("Ibrahim", 26, "UAM", 89)
teacher = Teacher("Maty", 48, "UAM", 1000000)

print()

members = [student, teacher]
for member in members:
    member.tell()

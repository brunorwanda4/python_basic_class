class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")

Student("Bruno", 20, "Computer Science").display_info()

Student("Happy", 19, "Kinyarwanda").display_info()

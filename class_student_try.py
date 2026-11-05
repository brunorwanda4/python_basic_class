class Student:
    def __init__(self, name, age , course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Course: {self.course}")

Student("John", 20, "Math").display_info()
Student("Bruno ", 20, "Medicine").display_info()

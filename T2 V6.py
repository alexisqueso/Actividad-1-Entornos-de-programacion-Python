class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hola! Soy un estudiante.")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hola, mi Id de estudiante es: {self.student_id}")

student = Student("Leydis", 21, "S2105")
student.greet()
    
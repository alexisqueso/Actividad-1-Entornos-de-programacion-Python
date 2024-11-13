class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hola, Yo soy {self.name}, tengo {self.age} años de edad, y mi Id de estudiante es {self.student_id}")

student = Student("Omar", 30, "S0521")
student.introduce()  

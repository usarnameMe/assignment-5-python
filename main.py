class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class CreateMixin:
    name: str
    surname: str
    age: int
    university: str

    def __str__(self):
        return f"name: {self.name}, surname: {self.surname}, age: {self.age}, university: {self.university}"


class Student(Person, CreateMixin):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university


student = Student(name="Gvn", surname="Uplisashvili", age=26, university="SkillWill University")
print(student)
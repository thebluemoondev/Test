class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __init__(self):
        self.name = ''
        self.age = 0

    def input(self):
        name = input("Nhập tên: ")
        age = input("Nhập tuổi: ")
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"


nnt = Person()
nnt.input()
print(nnt)
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"welcome {self.name} you are a {self.age} years old {self.age} ")


human = Person("chege", 23, "male")
human.introduce()

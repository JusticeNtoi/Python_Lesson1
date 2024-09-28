class Student:
    def __init__(self, name, major, gpa) -> None:
        self.name = name
        self.major = major
        self.gpa = gpa

    def on_honor_roll(self) -> bool:
        return self.gpa >= 3.5

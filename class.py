class Student:
    name = "Sharan"
    age = 21

s1 = Student()
s2 = Student()

print(s1.name)  # Sharan
print(s2.name)  # Sharan

"""
#once I added a constructor

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
Now:

s1 = Student("Sharan", 21)

s2 = Student("Kiran", 22)
"""
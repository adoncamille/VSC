
class Person():
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def __str__(self):
        s1 = self.name + " <=> " + str(self.age)
        return s1

    def Myfunc(self):
        print("{} a {} ans".format(self.name,self.age))

class Student(Person):
    pass

p2 = Student(35,"Alain")
p2.Myfunc()
print(p2)

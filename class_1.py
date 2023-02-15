class Person:
    
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def __str__(self):
    s1 = self.name + " and "
    s2 = str(self.age) 
    return s1 + s2

  def myfunc(self):
    print("Hello my name is " + self.name + " and my age is " + str(self.age))


class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
    # super().__init__(fname, lname)
    self.fname = "Alain"
    self.lname = " Yao"
    
p1 = Student("John", 36)
p1.myfunc()

print (p1)
print (p1.lname)
print (p1.fname)
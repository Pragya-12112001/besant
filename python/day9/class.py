class Student:
  def __init__(self, name, mark):
    self.name = name
    self.mark = mark
  
  def display(self):
    print(self.name, self.mark)

s1 = Student('pragya', 56)
s2 = Student('ananya', 45)

s1.display()
s2.display()
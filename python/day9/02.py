class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks
  
  def get_avg(self): # self is for Student 
    avg = sum(self.marks)//len(self.marks)
    print(self.name, avg)

s1 = Student('pragya', [45, 57, 98])

s1.get_avg()
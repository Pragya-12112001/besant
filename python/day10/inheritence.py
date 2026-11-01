class Employee:
  def work(self):
    print('performs work')
    
class Developer(Employee):
  def write_code(self):
    print('writes code')
    
d = Developer()
# d.work()
# d.write_code()

e = Employee()

e.work()

# multiple inheritence
# class Father:
#   def f_def(self):
#     return 'this is from father'
# class Mother:
#   def m_def(self):
#     return 'this is from mother'
  
# class Child(Father, Mother):
#   def c_def(self):
#     return 'child class is called'

# c = Child()
# print(c.c_def())
# print(c.f_def())
# print(c.m_def())
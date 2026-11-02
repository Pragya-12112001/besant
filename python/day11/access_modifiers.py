class Employee:
  def __init__(self, name, dept,  salary):
    self.name = name
    self._dept = dept  # Protected attribute
    self.__salary = salary  # Private attribute
    
  def display_details(self):
    print(self.name)
    print(self._dept)
    print(self.__salary)
    
e = Employee('ash', 'IT', 45000)
print(e.name)
print(e._dept)
# print(e.__salary) # gives error
print(e._Employee__salary) # use _CLASSNAME__privateVariable - this is called name mangling

# e.display_details()
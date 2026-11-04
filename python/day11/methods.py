class Employee:
  company_name = 'ABC Technologies'
  employee_count = 0
  min_salary = 10000
  
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.employee_count += 1
  
  # instance method
  def display_details(self):
    print('employee: ', self.name)
    print('salary: ', self.salary)
    print('company: ', Employee.company_name)
    
  # class method
  @classmethod
  def change_comany_name(cls, new_comapny):
    cls.company_name = new_comapny
    print('\n company name has been updated\n')
    
  # static method
  @staticmethod
  def is_valid_salary(salary):
    return salary >= Employee.min_salary
  
e1 = Employee('abc', 12000)
e2 = Employee('xyz', 1200)

print('name: ', e1.name, ',salary: ', e1.salary)

e1.display_details()

print('\n ----------------class method --------------')
print('\n ----------------after changing company name --------------')
e1.change_comany_name('xyz')
e1.display_details()


print('\n ----------------static method --------------')
print('name: ', e2.name, ',salary valid: ', e2.is_valid_salary(e2.salary))

# display total count using class level variable
print('\nemployee count: ', Employee.employee_count)
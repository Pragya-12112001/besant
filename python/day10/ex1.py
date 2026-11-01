# stu marks management
# 3 sub marks
# cal - total, avg, assign grades, identify top perdforming student
# generate report saved to txt file

class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks
    
  # cal total marks
  def total(self):
    return sum(self.marks)
  
  # cal avg  marks
  def avg(self):
    return round((self.total() / len(self.marks)), 2)
  
  # assign grade
  def cal_grade(self):
    if self.avg() >= 90:
      return 'A'
    elif self.avg() >= 75:
      return 'B'
    elif self.avg() >= 60:
      return 'C'
    elif self.avg() >= 40:
      return 'D'
    else:
      return 'F'
  
  # student report
  def report(self):
    return f'''
student name: {self.name}
marks: {self.marks}
total marks: {self.total()}
average: {self.avg()}
grade: {self.cal_grade()}\n
'''

  
# number of students
def get_student_count():
  while True:
    try:
      n = int(input('enter number of students: '))
      
      if n>=1:
        return n
      else:
        print('enter atleast 1 student')
  
    except ValueError:
      print('enter a valid whole number')

# marks validation
def get_valid_mark(sub):
  while True:
    try:
      mark = int(input(f'enter mark for {sub}: '))
      
      if 0 <= mark <= 100:
        return mark
      else:
        print(f'{sub} mark must be in the range of 0 and 100')
      
    except ValueError:
      print('invalid mark enter whole number only')

# name validation
def get_valid_name():
  while True:
    name = input('enter student name: ').strip()
    
    if name.isalpha():
      return name
    else:
      print('enter valid name - letters only')

# students details
def get_student_details():
  students = []
  n = get_student_count()

  for i in range(n):
    print(f'\n----------student {i+1}--------------\n')
    name = get_valid_name()
    marks = []
    
    for j in range(3):
      mark = get_valid_mark(f'mark in sub {j+1}')
      marks.append(mark)
    
    stu = Student(name, marks)
    students.append(stu)
  
  return students
    

# display students details/results
def display_results(students):
  print('---------------students result------------------')
  
  for student in students:
    print(student.report())

# top performing student
def get_top_performing_student(students):
  return max(students, key=lambda s: s.total())

# display top performer
def display_top_performer(student):
  print('-----------top performing student-----------------')
  print(student.report())
  
  
# save report / write in file
def save_report(students, top_student):
  with open('student_report.txt', 'w') as file:
    file.write('---------student marks report------------ \n')
    
    for student in students:
      file.write(student.report())
    
    file.write('---------top performer------------ \n')
    file.write(top_student.report())
    
  print('report saved successfully!!!!')
  
# read saved report 
def read_report():
  with open('student_report.txt', 'r') as file:
    content = file.read()
    print('----------------file content----------------')
    print(content)

# main function
def main():
  students = get_student_details()
  display_results(students)
  
  top_student = get_top_performing_student(students)
  display_top_performer(top_student)
  
  save_report(students, top_student)
  
  read_report()
  
  
# Program execution
if __name__ == "__main__":
    main()
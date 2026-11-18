# # square_list = [n**2 for n in range(1, 11)]
# # print(square_list)

# class Student:
#   def __init__(self, name, marks):
#     self.name = name
#     self.marks = marks

#   def details(self):
#     print(f'{self.name} : {self.marks}')
  
# s1 = Student('abc', [20, 23, 45])
# s1.details()

import time
import threading

def f1():
  time.sleep(2)
  print('f1')

def f2():
  print('f2')

c1 = threading.Thread(target=f1)
c2 = threading.Thread(target=f2)

c1.start()
c2.start()
c1.join()
c2.join()

print('done')
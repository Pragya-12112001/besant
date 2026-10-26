# this is used to reduce a list of numbers to a single value
from functools import reduce

def add(x, y):
  return x + y

marks = [10, 20, 30, 40, 50]
res = reduce(add, marks)
print(res)

# initial value can be provided to reduce function
res = reduce(add, marks, 100)
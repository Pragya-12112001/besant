num = [1, 2, 3, 4, 5, 6]

num_iterator = iter(num)

print(num_iterator)
print(type(num_iterator))
print(type(num))

try:
  print(next(num_iterator))
  print(next(num_iterator))
  print(next(num_iterator))
  print(next(num_iterator))
except StopIteration:
  print('no more elements are avaliable')
  
# custom iterator
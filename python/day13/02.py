def even_numbers():
  for i in range(1, 11):
    if i %2 == 0:
      yield i


# here we are actually calling next it does not have all the value it just have one value at time
# for value in even_numbers(): 
#   print(value)


def sample():
  return 'sam'
for i in sample():
  print(i)
  
  
def cal_total():
  for i in range(100001):
    yield i

total = 0
for i in cal_total():
  total += i
print(total)
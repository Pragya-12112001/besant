# higher order function
# function with a function as an argument

def double(x):
  return x * 2

l1 = [1, 2, 3, 4, 5]
res = map(double, l1)
print(list(res))
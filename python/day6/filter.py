# filter function
# keeps only those elements that satisfy the condition
def is_even(x):
  return x % 2 == 0

l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = filter(is_even, l2)
print(list(res))
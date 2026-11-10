# ex - 1
def numbers():
  for i in range(1, 11):
    yield i


for num in numbers():
  print(num)
  
# ex - 2
def odd_numbers():
  for i in range(1, 21):
    if i % 2 != 0:
       yield i


for num in odd_numbers():
  print(num)
  
# ex-3
def multiples(num):
    for i in range(1, 11):
        yield num * i


for value in multiples(5):
    print(value)
    
# ex - 4
def names_starting_with_a(names):
  for name in names:
    if name.startswith("A"):
      yield name


names = ["Alice", "Bob", "Ankit", "John", "Aman", "Priya"]

for name in names_starting_with_a(names):
  print(name)
    
# ex - 5
def numbers():
  yield 100
  yield 200
  yield 300


gen = numbers()

print(next(gen))
print(next(gen))
print(next(gen))
def cal(a ,b, /):
  return a+b

print(cal(10, 20))
# print(cal(a = 10, b = 20)) # here we will get error as / means we can only use positional only

def display(name, *, age):
  print(name, age)
  
display('pragya', age = 23)

def mix(name, / , age, *, city): # here age can be anything
  print(name, age, city)
  
mix('pragya', 23, city='abc')
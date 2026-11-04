def square(num):
  return num**2

def double(num):
  return num*2

def apply_operation(op, value):
  # res = op(value)
  # print('result: ' , res) 
  return f'result: {op(value)}'

print(apply_operation(square, 4))
print(apply_operation(double, 4))


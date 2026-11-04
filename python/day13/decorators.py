# call bacl function add functionality to the function and return enhanced version

def my_decorator(fun):
  def wrapper():
    print('fun execution started')
    
    fun()
    
    print('execution is completed')
    
  return wrapper # calling wrapper function

def cal():
  print(10+23)

calculate = my_decorator(cal)
# calculate()

# my_decorator(cal) this dosent work

@my_decorator
def add():
  print(23 + 34)
  
add()
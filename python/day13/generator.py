# generator
# produces values without storng
# used to return a sequence of values instead of a single value 
# yield:
  # Produces a value.
  # Pauses the function's execution.
  # Remembers where the function stopped.
  # Resumes execution when the next value is requested.


def get_numbers():
  yield 1
  yield 2
  yield 3
  yield 4
  yield 5
  
numbers = get_numbers()
print(numbers)

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
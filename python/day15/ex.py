# cerate dict containing num form 1 -10 as keys and there sq as values
res = {key: key ** 2 for key in range(1, 11) }
print(res)

# create dict from list of words using each word as key and there length as the value
words = ['hello', 'hey', 'are', 'you', 'there']
res = {word: len(word) for word in words}
print(res)


# 3
products = {
    "Laptop": 50000,
    "Mouse": 300,
    "Keyboard": 800,
    "Monitor": 12000,
    "USB": 400
}
result = {key: value for key, value in products.items() if value > 500}
print(result)


# 4
people = {
  "person1": "raipur",
  "person2": "delhi",
  "person3": "mumbai"
}
result = {key: value.upper() for key, value in people.items()}
print(result)


# 5
original = {
    "a": 1,
    "b": 2,
    "c": 3
}
result = {value: key for key, value in original.items()}
print(result)


# 6
numbers = [1, 2, 3, 4, 5, 6]
result = {number: "Even" if number % 2 == 0 else "Odd" for number in numbers}
print(result)


# 7
students = {
    "Aman": 85,
    "Riya": 45,
    "Rahul": 90,
    "Priya": 60,
    "Karan": 95
}
result = {name: marks for name, marks in students.items() if 60 <= marks <= 90}
print(result)


# 8
employees = ["Aman", "Riya", "Rahul", "Priya"]
salaries = [30000, 45000, 50000, 40000]
result = dict(zip(employees, salaries))
print(result)
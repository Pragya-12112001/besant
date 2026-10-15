# operators

a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)

a += 2
print(a)

# comparision and logical
age = 25
has_id = True

print(age>=18)
print(age<18)
print(age and has_id)
print(not has_id)
print(age>18 and has_id)
print(age<18 or has_id)
print(age<18 and has_id)

# membership operators
fruits = ['apple', 'banana', 'mango']

print('apple' in fruits)
print('apple' not in fruits)
print('ash' in fruits)
print('ash' not in fruits)

# identity operators
a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a == c)
print(a is c)
print(id(a) == id(b))
print(id(a))
print(id(b))
print(id(c))

# string operators
s = '   hello python    '
print(s[4])
print(s[-6])
print(s.split())
print(s.strip())
print(s[4: 8])

# logical operators

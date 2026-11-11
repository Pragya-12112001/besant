words = ['python', 'java', 'sql']

res = {word : len(word) for word in words}
print(res)

marks = {'a': 23, 'b': 67, 'c': 76}

res = {
    name: 'pass' if score > 33 else 'fail'
    for name, score in marks.items()
}

print(res)



names = ['Pragya', 'Rahul', 'Aman']
scores = [85, 90, 78]

print(list(zip(names, scores)))
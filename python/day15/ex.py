# cerate dict containing num form 1 -10 as keys and there sq as values
res = {key: key ** 2 for key in range(1, 11) }
print(res)

# create dict from list of words using each word as key and there length as the value
words = ['hello', 'hey', 'are', 'you', 'there']
res = {word: len(word) for word in words}
print(res)
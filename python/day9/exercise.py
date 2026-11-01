def ex1(inp, target):
  list1 = list(inp.lower().split())
  print(list1)

  longest_word = ''

  for i in list1:
    if len(i)>len(longest_word):
      longest_word = i
  print('longest word: ', len(longest_word))
  count = 0

  for i in inp:
    if i == target:
      count += 1
  print(count)

  print(inp.count(target))

inp = 'hey there how are you'
# inp = input('enter your sentence: ')

target = 'h'
# target = input('enter the target char: ')

ex1(inp, target)
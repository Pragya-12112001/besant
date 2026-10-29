# list 

# even and odd lists
# largest and smallest
# sum and avg
# count of positive and negative

# inp = list(map(int, input().split()))
# print(inp)

n = int(input('enter len of list: '))

l = []

for i in range(n):
  l.append(int(input()))

print(l)

odd = []
even = []
pos_count = 0
neg_count = 0
for i in l:
  if i>0:
    pos_count += 1
  else:
    neg_count += 1
  if i%2 == 0:
    even.append(i)
  else:
    odd.append(i)
    
print(f'odd list {odd}')
print(f'even list {even}')

print(f'largest {max(l)}')
print(f'samllest {min(l)}')
print(f'sum {sum(l)}')

avg = sum(l) / n
print(f'average {avg}')

print(f'positive count = {pos_count}')
print(f'negitive count = {neg_count}')
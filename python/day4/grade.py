# use if-elif-else a(90+), b(75-89), c(60-74), d below 60

n = int(input('enter score: '))
score = ''

if n>=90:
  score = "A"
  # print('A')
elif n>=75:
  score = "B"
elif n>=60:
  score = "C"
else:
  score = "D"
  
print(score)
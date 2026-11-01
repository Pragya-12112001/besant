# acronym
# first char 

inp = 'National aeronautics and space administration'
# inp = input('enter the sentence: )

def acronym(inp):
  l1 = inp.split()
  unwanted = ('is', 'an', 'and', 'or', 'the', 'this', 'that')
  wanted = []
  
  for i in l1:
    if i in unwanted:
      continue 
    else:
      wanted.append(i[0])
  print(('').join(wanted).upper())

acronym(inp) 
  
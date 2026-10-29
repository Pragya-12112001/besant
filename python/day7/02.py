# with open('write.txt', 'w') as file:
  # file.write('shopping list \nbread \n')
  
# with open('write.txt', 'a') as file:
#   file.write('new append content')

# create a file 
# the file should not be existing
with open('new.txt', 'x') as file:
  file.write('new file')
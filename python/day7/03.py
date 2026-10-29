with open('new.txt', 'r+') as f:
  # can update the content
  old_content = f.read()
  print(f.seek(0))
  
  f.write('\nupdated notes using r+')
  print(f.seek(0))
  print(f.read())
# to run the file we have to be in day7 folder other wise it wil throw file not found error

# file = open('notes.txt', 'r')
# content = file.read()
# print(content)
# file.close()

# context manager
with open('notes.txt', 'r') as file:
    content = file.read()
    # print(content)
    
    # readline functions
    file.seek(0)
    # brings back the pointer to start 0
    line = file.readline()
    print(line)
    
    print(file.read(4)) # as the pointer is now not on 0
    print(file.tell()) # to get current pointer position
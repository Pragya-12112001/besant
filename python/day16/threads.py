import time
import threading

def walk_dog():
    time.sleep(8)
    print('you finish walking the dog')

def trash_takeout():
    time.sleep(4)
    print('you took the trash out')

def get_mail():
    time.sleep(2)
    print('you got the mail')

chore1 = threading.Thread(target=walk_dog)
chore2 = threading.Thread(target=trash_takeout)
chore3 = threading.Thread(target=get_mail)

chore1.start()
chore2.start()
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print('all statements are completed')
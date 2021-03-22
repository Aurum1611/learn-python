from threading import Thread,current_thread

def dispNumbers():
    print(current_thread().getName())
    for i in range(0,11):
        print(i)

print(current_thread().getName())
t=Thread(target=dispNumbers)
t.start()
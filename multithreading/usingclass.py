from threading import Thread,current_thread
from time import sleep

class AnotherThread:
    def dispNumbers(self):
        print(current_thread().getName())
        sleep(1)
        for i in range(0,30,5):
            print(i)

obj=AnotherThread()
t=Thread(target=obj.dispNumbers)
t.start()

t2=Thread(target=obj.dispNumbers)
t2.start()

t3=Thread(target=obj.dispNumbers)
t3.start()

t4=Thread(target=obj.dispNumbers)
t4.start()
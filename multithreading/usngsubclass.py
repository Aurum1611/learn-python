from threading import Thread,current_thread

class MyThread(Thread):
    def run(self):
        print(current_thread().getName())
        for i in range(0,21,2):
            print(i)

t=MyThread()
t.start()
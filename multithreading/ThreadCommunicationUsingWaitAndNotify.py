from threading import Thread, current_thread, Condition
from time import sleep

class Producer:
    
    def __init__(self):
        self.products=[]
        self.cond=Condition()
        
    def produce(self):
        print(current_thread())
        self.cond.acquire()
        for i in range(1,8):
            self.products.append("Item"+str(i))
            print("item added")
            sleep(1)
        print("Products are ready")
        self.cond.notify()
        self.cond.release()

class Consumer:
    
    def __init__(self,prod):
        self.prod=prod
    
    def consume(self):
        print(current_thread())
        self.prod.cond.acquire()
        self.prod.cond.wait(timeout=0)
        print("Shipping in progress")
        self.prod.cond.release()
        print("Products being shipped are",self.prod.products)
    
prod=Producer()
cons=Consumer(prod)

t1=Thread(target=prod.produce)
t2=Thread(target=cons.consume)

t1.start()
t2.start()
from threading import Thread, current_thread
from time import sleep

class Producer:
    
    def __init__(self):
        self.products=[]
        self.shipmentReady=False
        
    def produce(self):
        print(current_thread())
        for i in range(1,8):
            self.products.append("Item"+str(i))
            print("item added")
            sleep(1)
        print("Products are ready")
        self.shipmentReady=True

class Consumer:
    
    def __init__(self,prod):
        self.prod=prod
    
    def consume(self):
        print(current_thread())
        while self.prod.shipmentReady==False:
            sleep(0.2)
        
        print("Shipping in progress")
        print("Products being shipped are",self.prod.products)
    
prod=Producer()
cons=Consumer(prod)

t1=Thread(target=prod.produce)
t2=Thread(target=cons.consume)

t1.start()
t2.start()
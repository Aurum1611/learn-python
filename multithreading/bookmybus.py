from threading import Thread,Semaphore#,Lock

class BookMyBus:
    
    def __init__(self,availableSeats):
        self.availableSeats = availableSeats
        self.l=Semaphore() #Lock()
    
    def runThis(self,seatsRequested):
        self.l.acquire()
        if self.availableSeats>=seatsRequested:
            print("Total number of available seats:",self.availableSeats)
            print("Confirming the seat")
            print("Payment in progress")
            print("Payment Successful")
            self.availableSeats-=seatsRequested
            print("Please do visit again")
        else:
            print("Total number of available seats:",self.availableSeats)
            print("Requested number of seats ("+str(seatsRequested)+") are not available")
        self.l.release()

t=BookMyBus(10)

t1=Thread(target=t.runThis,args=(3,))
t2=Thread(target=t.runThis,args=(2,))
t3=Thread(target=t.runThis,args=(1,))
t4=Thread(target=t.runThis,args=(1,))
t5=Thread(target=t.runThis,args=(4,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
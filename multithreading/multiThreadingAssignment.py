from threading import Thread

def evenNumbersThread():
    for i in range(1,101):
        if i%2==0:
            print(i)

def oddNumbersThread():
    for i in range(1,101):
        if i%2!=0:
            print(i)

ev=Thread(target=evenNumbersThread,name="Even Numbers Thread")
od=Thread(target=oddNumbersThread,name="Odd Numbers Thread")

ev.start()
od.start()

for i in range(1,101):
    print(i)

from datetime import date
from time import sleep,perf_counter

startTime=perf_counter()

datesList=[]

datesList.append(date(2033,7,26))
datesList.append(date(2035,7,24))
datesList.append(date(2021,4,6))
datesList.append(date(2035,7,24))
datesList.append(date(2021,4,6))
datesList.append(date(2029,5,13))
datesList.append(date(2027,4,3))

datesList.sort()

sleep(3)

for x in datesList:
    print(x)

endTime=perf_counter()
print("Execution Time: %.5f"%(endTime-startTime))
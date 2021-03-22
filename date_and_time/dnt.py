import time, datetime

epochseconds=time.time()
print(epochseconds)

today=time.ctime(epochseconds)
print(today)

dObj=datetime.datetime.today()
print(dObj.date())
print("Current date: {}/{}/{}".format(dObj.day,dObj.month,dObj.year))
print("Current time: {}:{}:{}".format(dObj.hour,dObj.minute,dObj.second))

from datetime import date,time,datetime

dt=date(3031,11,2)
tm=time(23,0)
dttm=datetime.combine(dt,tm)
print(dttm)
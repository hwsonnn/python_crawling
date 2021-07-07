from datetime import date, time, datetime, timedelta

#ctime = datetime.now()
ctime = datetime.now() - timedelta(days=1)
                    # - timedelta(days=1) 을 추가함으로써 어제 날짜 출력됨.


print(ctime)
print(type(ctime))
print(ctime.year)
print(ctime.month)
print(ctime.day)
print(ctime.strftime('%Y%m%d'))



































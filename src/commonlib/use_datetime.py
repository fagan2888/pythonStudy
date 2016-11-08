from datetime import datetime, timezone, timedelta

now = datetime.now()
print(now)
print(type(now))
stamp = now.timestamp()
print('当前时间戳 %s' % stamp)
# timestamp转换为datetime
print('本地时间 %s' % datetime.fromtimestamp(stamp))
# timestamp转换为UTC标准时间datetime
print('UTC时间 %s' % datetime.utcfromtimestamp(stamp))

# 获取指定日期和时间
dt = datetime(2016, 10, 31, 13, 27, 22, 125000, timezone(timedelta(hours=8)))
print(dt)

# str转换为datetime
cday = datetime.strptime('2016-10-31 15:25:22', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
currentTime = datetime.now()
print(currentTime.strftime('%Y %A %B %d %H:%M'))

# datetime加减
addHours = 8
addDays = 8
addWeeks = 8
addMintes = 8
print('增加 %d 分钟: %s' % (addHours, currentTime + timedelta(minutes=addMintes)))
print('增加 %d 小时: %s' % (addHours, currentTime + timedelta(hours=addHours)))
print('增加 %d 天: %s' % (addHours, currentTime + timedelta(days=addDays)))
print('增加 %d 周: %s' % (addHours, currentTime + timedelta(weeks=addWeeks)))

print(currentTime.utcnow())

# 拿到utc时间并强制设置时区为UTC+0:00
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('UTC+0:00 时区为: %s' % utc_dt)
# astimezone()将utc时区转换为北京时间
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('北京时间: %s' % bj_dt)
# astimezone()将utc时区转换为东京时间
tokyo_dt= utc_dt.astimezone(timezone(timedelta(hours=9)))
print('东京时间：%s' % tokyo_dt)
# 将北京时间转换为东京时间
print('东京时间：%s' % bj_dt.astimezone(timezone(timedelta(hours=9))))

# print(datetime(2015, 5, 18, 17, 2, 10, 871012, tzinfo=timezone(timedelta(0, 28800))))
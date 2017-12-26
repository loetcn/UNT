
import time

SECONDS_PER_DAY = 24 * 60 * 60

def doFunc():
    print("do Function...")

def doFirst(hour , minute , second , microsecond = 0 ):
    from datetime import datetime, timedelta
    curTime = datetime.now()
    desTime = curTime.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)
    delta = curTime - desTime
    skipSeconds = SECONDS_PER_DAY - delta.total_seconds()
    print("Must sleep %d seconds" %skipSeconds)
    return skipSeconds


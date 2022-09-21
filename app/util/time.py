# Determine if the time between two datetimes is greater than a given number of hours
from datetime import datetime, timedelta

def is_time_between_greater_than_hours(datetime1: datetime, datetime2: datetime, hours: int) -> bool:
    time_between = datetime1 - datetime2
    return time_between > timedelta(hours=hours)

def is_time_between_greater_than(datetime1: datetime, datetime2: datetime, time_limit: timedelta) -> bool:
    time_between = datetime1 - datetime2
    return time_between > time_limit
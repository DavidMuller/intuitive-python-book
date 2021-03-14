# alternatively: `from backports.zoneinfo import ZoneInfo` if you
# are on Python <= 3.9 and have installed backports.zoneinfo
from zoneinfo import ZoneInfo

def is_aware(dt_value):
    """Returns True if dt_value is timezone aware. False otherwise"""
    return (
        dt_value.tzinfo is not None
        and dt_value.tzinfo.utcoffset(dt_value) is not None
    )

def make_aware(dt_value, timezone_name):
    """Make dt_value an aware datetime in the given timezone_name"""
    if is_aware(dt_value):
        raise ValueError("dt_value is already aware")
    zone_info = ZoneInfo(timezone_name)
    return dt_value.replace(tzinfo=zone_info)

def change_timezone(dt_value, timezone_name):
    """
    Change the timezone associated to dt_value to the given timezone_name
    """
    if not is_aware(dt_value):
        raise ValueError("Must pass a timezone aware dt_value")
    zone_info = ZoneInfo(timezone_name)
    return dt_value.astimezone(zone_info)

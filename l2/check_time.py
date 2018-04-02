import datetime
def check_time(func, *args):
    time1_s = datetime.datetime.now()
    result = func(*args)
    time2_s = datetime.datetime.now()
    return "{}\n".format(time2_s-time1_s), result

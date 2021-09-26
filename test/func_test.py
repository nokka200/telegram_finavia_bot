import datetime


def date_fixer(date, hour_fix=3, debug=False):
    # This function will try to make a datetime object from parameter date

    try:
        date = date[0:-1]
        date_time = datetime.datetime.fromisoformat(date)

        # this adds the extra h to Z time zone
        date_time_delta = datetime.timedelta(hours=hour_fix)
    except:
        return False

    if debug:
        print(f"date_fixer.date_time: {date_time}")
        print(f"date_fixer.date_time.now: {date_time.now()}")

    return date_time + date_time_delta


def time_fixer(date_obj, format="%H:%M"):
    # This function will try to format the date_obj

    try:
        fixed = date_obj.strftime(format)
    except AttributeError:
        return "-"

    return fixed


def status_fixer(status):
    if status == None:
        return "-"
    else:
        return status

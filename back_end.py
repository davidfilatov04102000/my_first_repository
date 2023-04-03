def shet(arg):
    time_in_sec = 5900000000 / arg
    time_in_min = time_in_sec / 60
    time_in_ocl = time_in_min / 60
    time_in_day = time_in_ocl / 24
    time_in_month = time_in_day / 30
    time_in_year = time_in_month / 12
    return round(time_in_year)

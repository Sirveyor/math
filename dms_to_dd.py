def dms_to_dd(value):
    degs = float(value.split('.')[0])
    mins = float((value.split('.')[1])[:2])
    secs = float((value.split('.')[1])[2:])

    return((secs / 60 + mins) / 60 + degs)


from datetime import datetime

import pytz

OTHER_TIMEZONES = [
    pytz.timezone('US/Eastern'),
    pytz.timezone('Pacific/Auckland'),
    pytz.timezone('Asia/Calcutta'),
    pytz.timezone('UTC'),
    pytz.timezone('Europe/Paris'),
    pytz.timezone('Africa/Khartoum'),
]
fmt = '%Y-%m-%d %H:%M:%S %Z%z'

while True:
    date_input = input("When is your meeting? Please use MM/DD/YY HH:MM format. ")
    try:
        local_date = datetime.strptime(date_input, '%m/%d/%Y %H:%M')
    except ValueError:
        print("{} doesn't seem to be a valid date and time.".format(date_input))
    else:
        local_date = pytz.timezone('US/Pacific').localize(local_date)  # localize: make a naive datetime aware
        utc_date = local_date.astimezone(pytz.utc)  # set the aware as the foundational tz
        output = []
        for timezone in OTHER_TIMEZONES:
            output.append(utc_date.astimezone(timezone))
        for appointment in output:
            print(appointment.strftime(fmt))
        break
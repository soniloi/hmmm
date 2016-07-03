#!/usr/bin/env python

import time
import datetime

RETIREMENT_AGE = 65 # TODO: per-country

dob_cal = raw_input("What is your date of birth (dd/mm/yyyy)? ").split("/")
dob_year = int(dob_cal[2])
dob_month = int(dob_cal[1])
dob_day = int(dob_cal[0])

dob_unix = time.mktime(datetime.date(dob_year, dob_month, dob_day).timetuple())
dor_unix = time.mktime(datetime.date(dob_year + RETIREMENT_AGE, dob_month, dob_day).timetuple())
today_unix = time.time()

print "dob: " + str(dob_unix)
print "dor: " + str(dor_unix)
print "today: " + str(today_unix)
print "seconds until retirement: " + str(dor_unix - today_unix)

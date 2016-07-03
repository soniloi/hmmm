#!/usr/bin/env python

import time
import datetime

SECONDS_PER_DAY = 86400
DAYS_PER_WEEK = 7
WORKING_DAYS_PER_WEEK = 5

RETIREMENT_AGE = 68 # TODO: per-country
PUBLIC_HOLIDAYS_MONDAY = 5 # Number of public holidays each year that always fall on a Mondays
PUBLIC_HOLIDAYS_OTHER = 4 # Number of public holidays each year that may fall on any day
ANNUAL_LEAVE_DAYS = 20

dob_cal = raw_input("What is your date of birth (dd/mm/yyyy)? ").split("/")
dob_year = int(dob_cal[2])
dob_month = int(dob_cal[1])
dob_day = int(dob_cal[0])

dob_unix = time.mktime(datetime.date(dob_year, dob_month, dob_day).timetuple())
dor_unix = time.mktime(datetime.date(dob_year + RETIREMENT_AGE, dob_month, dob_day).timetuple())
today_unix = time.time()

seconds_until = dor_unix - today_unix
days_until = seconds_until / SECONDS_PER_DAY
working_days_until = days_until * WORKING_DAYS_PER_WEEK / DAYS_PER_WEEK

print "Key dates:"
print "\tdob: " + str(dob_unix)
print "\tdor: " + str(dor_unix)
print "\ttoday: " + str(today_unix)
print "Until retirement:"
print "\tseconds: " + str(seconds_until)
print "\tdays: " + str(days_until)
print "\tworking days: " + str(working_days_until)

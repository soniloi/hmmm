#!/usr/bin/env python

import time
import datetime

SECONDS_PER_DAY = 86400.0
AVERAGE_SECONDS_PER_YEAR = SECONDS_PER_DAY * 365.25
DAYS_PER_WEEK = 7.0
WORKING_DAYS_PER_WEEK = 5.0

RETIREMENT_AGE = 68 # TODO: per-country
PUBLIC_HOLIDAYS_MONDAY = 5.0 # Number of public holidays each year that always fall on a Mondays
PUBLIC_HOLIDAYS_OTHER = 4.0 # Number of public holidays each year that may fall on any day
ANNUAL_LEAVE_DAYS = 20.0

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
mondays_until = working_days_until / 5

years_until = seconds_until / AVERAGE_SECONDS_PER_YEAR

# Some public holidays are guaranteed to fall on Mondays; others may fall on any (working) day
annual_public_holiday_monday = PUBLIC_HOLIDAYS_MONDAY + PUBLIC_HOLIDAYS_OTHER / WORKING_DAYS_PER_WEEK

# Assume user equally likely to take annual leave on any of the working days of the week
annual_leave_monday = ANNUAL_LEAVE_DAYS / WORKING_DAYS_PER_WEEK

total_monday_leave = years_until * (annual_public_holiday_monday + annual_leave_monday)
working_mondays_until = int(round(mondays_until - total_monday_leave))

print "Key timestamps:"
print "\tDOB: " + str(dob_unix)
print "\tDOR: " + str(dor_unix)
print "\tToday: " + str(today_unix)
print "Until retirement:"
print "\tSeconds: " + str(seconds_until)
print "\tYears: " + str(years_until)
print "\tDays: " + str(days_until)
print "\tWorking days: " + str(working_days_until)
print "\tMondays: " + str(mondays_until)
print "\tEstimated Working Mondays: " + str(working_mondays_until)

"""
This program calculates the total number of seconds in a year.

"""

days_per_year = 365
hours_per_day = 24
minutes_per_hour = 60
seconds_per_minute = 60

def seconds_in_year():
    print("There are "+ str(days_per_year * hours_per_day * minutes_per_hour * seconds_per_minute) + " seconds per year")
seconds_in_year()
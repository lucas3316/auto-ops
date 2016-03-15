#!/usr/bin/env python
# coding:utf8

import time
import datetime
from dateutil.relativedelta import relativedelta

def format_time(t,format1,format2):
	return time.strftime(format2,time.strptime(format1,t))

def readableTime(time_second):
    days = time_second // 86400
    day = str(days)+'d' if days else ''
    hours = time_second // 3600 % 24
    hour = str(hours)+'h' if hours else ''
    mins = time_second // 60 % 60
    min = str(mins)+'m' if mins else ''
    secs = time_second % 60
    sec = str(secs)+'s' if secs else ''
    return day+hour+min+sec

def getlastweek():
    today = datetime.date.today()
    weekday = today.weekday()
    start_delta = datetime.timedelta(days=weekday,weeks=1)
    start_of_week = today-start_delta
    end_of_week = start_of_week+datetime.timedelta(7)
    start_of_week_strftime = start_of_week.strftime('%Y-%m-%d')
    end_of_week_strftime = end_of_week.strftime('%Y-%m-%d')
    start_of_week_timestamp = int(time.mktime(start_of_week.timetuple()))
    end_of_week_timestamp = int(time.mktime(end_of_week.timetuple()))
    return start_of_week_timestamp,end_of_week_timestamp,start_of_week_strftime,end_of_week_strftime

def getlastmonth():
    today = datetime.date.today()
    d = today - relativedelta(months=1)
    start_of_month = datetime.date(d.year,d.month,1)
    end_of_month = datetime.date(today.year,today.month,1)
    start_of_month_strftime = start_of_month.strftime('%Y-%m-%d')
    end_of_month_strftime = end_of_month.strftime('%Y-%m-%d')
    start_of_month_timestamp = int(time.mktime(start_of_month.timetuple()))
    end_of_month_timestamp = int(time.mktime(end_of_month.timetuple()))
    return start_of_month_timestamp,end_of_month_timestamp,start_of_month_strftime,end_of_month_strftime
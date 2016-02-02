#!/usr/bin/env python
# coding:utf8

import time

def format_time(t,format1,format2):
	return time.strftime(format2,time.strptime(format1,t))
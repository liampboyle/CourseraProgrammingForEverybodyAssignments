#-------------------------------------------------------------------------------
# Name:        Programming for Everybody (Python) Assignment 3.1
# Purpose: "Write a program to prompt the user for hours and rate per hour using
# raw_input to compute gross pay. Award time-and-a-half for the hourly rate for
# all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to
# test the program (the pay should be 498.75). You should use raw_input to read
# a string and float() to convert the string to a number. Do not worry about
# error checking the user input - assume the user types numbers properly."
#
# Author:      Liam Boyle
#
# Created:     20/06/2014
# Copyright:   No Copyright
# Licence:     Open - Please Steal This Program
#-------------------------------------------------------------------------------

FULLHOURS = 40.0
hoursStr = raw_input("Enter Hours:")
hours = float(hoursStr)
rateStr = raw_input("Enter Rate:")
rate = float(rateStr)

if hours <= FULLHOURS:
    pay = hours * rate
else:
    otHours = hours - FULLHOURS
    otRate = rate * 1.5
    pay = rate * FULLHOURS + otHours * otRate

print "Pay Equals:",pay

#financial_calculator.py
#Goal: Script for solving time-value money problems
#Author: Paritosh Dash
#Created: May-16th-2020
#---------------------------------------------------------------

import numpy as np
import sys

print("\n0.PV\n1.FV\n2.Rate\n3.N\n4.PMT")
choice = input("\nChoose what solve to for: ")

if(choice=="0"):
    print("\nEnter values as prompted")
    print("Enter interest rate as decimal")
    n = input("\nEnter times compounded: ")
    rate = input("\nEnter rate as decimal: ")
    fv = input("\nEnter FV: ")
    pmt = input("\nEnter Pmt: ")
    time_range = input("\nEnter number of years: ")
    if(float(time_range)==0 or float(time_range)<0):
        print("\nError: Must be a minimum of 1 year")
    else:
        pv=np.pv(float(rate)/float(n), float(time_range)*float(n), float(pmt), float(fv))
        print("PV: "+str(pv))
        
elif(choice=="1"):
    print("\nEnter values as prompted")
    print("Enter interest rate as decimal")
    n = input("\nEnter times compounded: ")
    rate = input("\nEnter rate as decimal: ")
    pv = input("\nEnter PV: ")
    pmt = input("\nEnter Pmt: ")
    time_range = input("\nEnter number of years: ")
    if(float(time_range)==0 or float(time_range)<0):
        print("\nError: Must be a minimum of 1 year")
    else:
        fv=np.fv(float(rate)/float(n), float(time_range)*float(n), float(pmt), float(pv))
        print("FV: "+str(fv))
elif(choice=="2"):
    print("\nEnter values as prompted")
    print("Enter interest rate as decimal")
    n = input("\nEnter times compounded: ")
    pv = input("\nEnter PV: ")
    fv = input("\nEnter FV: ")
    pmt = input("\nEnter Pmt: ")
    time_range = input("\nEnter number of years: ")
    if(float(time_range)==0 or float(time_range)<0):
        print("\nError: Must be a minimum of 1 year")
    else:
        rate=np.rate(float(time_range)*float(n), float(pmt), float(pv), float(fv))
        print("Rate: "+str(rate))
elif(choice=="3"):
    print("\nEnter values as prompted")
    print("Enter interest rate as decimal")
    pv = input("\nEnter PV: ")
    rate = input("\nEnter rate as decimal: ")
    fv = input("\nEnter FV: ")
    pmt = input("\nEnter Pmt: ")
    time_range = input("\nEnter number of years: ")
    if(float(time_range)==0 or float(time_range)<0):
        print("\nError: Must be a minimum of 1 year")
    else:
        n=np.nper(float(rate), float(pmt), float(pv), float(fv))
        print("Number of Periods: "+str(n))
elif(choice=="4"):
    print("\nEnter values as prompted")
    print("Enter interest rate as decimal")
    n = input("\nEnter times compounded: ")
    rate = input("\nEnter rate as decimal: ")
    fv = input("\nEnter FV: ")
    pv = input("\nEnter PV: ")
    time_range = input("\nEnter number of years: ")
    if(float(time_range)==0 or float(time_range)<0):
        print("\nError: Must be a minimum of 1 year")
    else:
        pmt=np.pmt(float(rate), float(n)/float(time_range), float(pv), float(fv))
        print("Payment: "+str(pmt))
else
    print("Error: Must choose options 0-4.")
    
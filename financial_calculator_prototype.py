import numpy as np
import sys

#Instructions for user
print("Enter values as prompted")
print("Enter interest rate as decimal")
print("Leave blank for value you would like calculated")

#Get user input
pv = input("Enter PV: ")
n = input("Enter times compounded: ")
rate = input("Enter rate as decimal: ")
fv = input("Enter FV: ")
pmt = input("Enter Pmt: ")
time_range = input("Enter number of years: ")

#print(pv, n, rate, fv, pmt, time_range)

#sys.exit("Stopped")

#define functions for calculating financials
#when = 'end' is when the calcution is made, beginning or end of period
def single_pv(pv, n, rate, fv, pmt):
    float(fv)
    float(n)
    float(rate)
    float(pmt)
    float(time_range)
    pv=np.pv(rate, n, pmt, fv, when = 'end')
    print(pv)
    
def single_fv(pv, n, rate, fv, pmt):
    fv=np.fv(rate/n, n, pmt, pv, when = 'end')
    
def single_period(pv, n, rate, fv, pmt):
    n=np.nper(rate/n, pmt, pv, fv, when = 'end')
    
def single_rate(pv, n, rate, fv, pmt):
    np.rate(n, pmt, pv, fv, when = 'end')
    
def single_pmt(pv, n, rate, fv, pmt):
    np.pmt(rate/n, n, pv, fv, when = 'end')


#determine what value user needs solved
if(len(pv) == 0):
    print("PV is empty")
    #single_pv(pv, n, rate, fv, pmt)
elif(len(fv) == 0):
    print("FV is empty")
elif(len(n) == 0):
    print("n is empty")
elif(len(rate) == 0):
    print("rate is empty")
elif(len(pmt) == 0):)
    print("pmt is empty")
            
        
'''
#program to prompt the user for hours and rate per hour to compute gross pay
hours = int(input("Enter hours:"))
rate = float(input("Enter rate:"))
pay = int(input("Enter pay:"))
pay = hours*rate
print("pay",pay)
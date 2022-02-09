'''
salary=float(input('enter the salary:'))
years=int(input('enter the years of service:'))
if years>10:
    print('net bonus is:',10/100*salary)
elif years>=6 and years<=10:
    print('net bonus is:',8/100*salary)
else:
    print('net bonus is:',5/100*salary)

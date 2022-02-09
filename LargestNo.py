'''
a=int(input('enter a value for a:'))
b=int(input('enter a value for b:'))
c=int(input('enter a value for c:'))
if a>b and a>c:
    print('The largest number is:',a)
if b>c and b>a:
    print('The largest number is:',b)
if c>a and c>b:
    print('The largest number is:',c)
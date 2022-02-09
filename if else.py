#program to grade the system
maths = float(input("enter maths"))
english = float(input("enter english"))
kiswahili = float(input("enter kiswahili"))
science = float(input("enter science"))
cre = float(input("enter cre"))
total=maths+english+kiswahili+science+cre
average=total/5
if average>=70 and average<=100:
    print('A')
elif average<=69 and average<=50:
    print('B')
elif average<=49 and average<=40:
    print('C')
elif average<=39 and average<=30:
    print('D')
else:
    print('fail')
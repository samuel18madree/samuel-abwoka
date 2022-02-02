
print (21//5)
print (21/5)
print (26//9)
print (26/9)

#Arithmetic operators
a=10
b=5
print ("addition",a+b)
print ("subtraction",a-b)
print ("multiplication",a*b)
print ("division",a/b)
print ("floor division",a//b)
print ("modulus",a%b)
print ("exponent",a**b)


#program to prompt the userto enter a number divisible by 2
number = int(input("Enter a number:"))
if number % 2 == 0:
    print("Even")
else:
    print("odd")

#program to prompt the userto enter a number divisible by 5
number = int(input("Enter a number:"))
if number % 5 == 0:
    print("Even")
else:
    print("odd")


#program to prompt the userto enter a number divisible by 5,7,11
number = int(input("Enter a number:"))
if number % 5 == 0:
    print("Even")
else:
    print("odd")
if number % 11 == 0:
    print ("Even")
else:
    print ("odd")
if number % 7 == 0:    
    print("Even")
else:
    print("odd")


#program to assign a discount of 5% if amount of purchase exceeds sh 1000
amount = int(input("Enter amount:"))
if amount > 1000:
    discount = 0.05*amount
    print ("discount is:",discount)
else:
    print("sorry rich guy:")


#program to prompt the if a person is eligible to vote.
age = int(input("Enter age:"))
nationality = str(input("Enter nationality:"))
if age>=18 and nationality == "kenyan":
    print ("eligible")
else:
    print ("not eligible")


#program to check if you are eligible tovote
age = int(input('Enter age:'))
nationality = input('Enter your country:').upper()
country = ['KENYA','TANZANIA','UGANDA']
if nationality in  country  and age >= 18:
    print('Eligible to vote')
else:
    print('Not Eligible to vote')

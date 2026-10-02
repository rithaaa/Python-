#LOOPING STATEMENTS

#WHILE LOOP

'''1 2 3 4  5 6 7 8 9 10'''

##i=1
##while i<=10:
##    print(i,end=" ")
##    i+=1


'''10 9 8 7 6 5 4 3 2 1'''

##i=10
##while i>=1:
##    print(i, end=" ")
##    i-=1
    


''' WAP to print even numbers from 1 to 50.'''

##i=2
##while i<=50:
##    print(i, end=" ")
##    i+=2



''' WAP to print numbers divisible by 10 from 1 to 100.'''

##i=10
##while i<=100:
##    print(i, end=" ")
##    i+=10



'''WAP to print the sum of n natural numbers.'''

##n=int(input("Enter number: "))
##i=1
##sum=0
##while i <= n:
##    sum+=i
##    i+=1
##print(sum)


#OR


##n=int(input("Enter n: "))
##total=0
##while n>0:
##    total+=n
##    n-=1
##print("SUM: ",total)



'''1.WAP to print the following using while loop, First 10 even number.'''

##i=2
##while i<21:
##    print(i,end=" ")
##    i+=2


'''WAP  to print first 10 odd numbers.'''

##i=1
##while i<20:
##    print(i,end=" ")
##    i+=2


'''WAP to print first 10 integers and their squares using while loop.'''

##i=1
##while i<11:
##    print(i,i**2,sep=" ")
##    i+=1


'''Write a while loop statement to print the following series: 10,20,30,....300.'''

##i=10
##while i<=300:
##    print(i,end=" ",sep=" ")
##    i+=10


'''Write a while loop statement to print the following series 105,98,91,....7.'''

##i=105
##while i>0:
##    print(i,end=" ",sep=" ")
##    i-=7
    

'''WAP to reverse a number without using typecasting.'''

##n=int(input("Enter number: "))         #123
##rev=0
##while n>0:                             #123>0  #12>0  #1>0
##    last=n%10                          #3   #2  #1
##    rev=rev*10+last                    #0*10+3   #3*10+2=32  #32*10+1=321
##    n//=10                             #12  #1  #0
##print("Reversed Number: ",rev)



'''Find the sum of individual digits of a number.'''

##n=int(input("Enter number: "))
##sum=0
##while n>0:
##    last=n%10
##    sum+=last
##    n//=10
##print("SUM: ",sum)


'''WAP to find the product of individual digits of a number.'''

##n=int(input("Enter number: "))
##pdt=1
##while n>0:
##    last=n%10
##    pdt*=last
##    n//=10
##print("Product: ",pdt)



'''WAP to find the factorial of a number.'''

##n=int(input("Enter number" ))
##fact=1
##while n>0:
##    fact*=n
##    n-=1
##print("Factorial: ",fact)

#OR

##n=int(input("Enter number: "))
##i=1
##fact=1
##while i<=n:
##    fact*=i
##    i+=1
##print("Factorial: ",fact)



'''WAP to find the sum of all integers present in the list.'''
''' l=[1,2,3,'hello','hi',[1,2],30,70,30.2]'''

##l=eval(input("Enter the list: "))
##i=0
##sum=0
##while i<len(l):
##    if type(l[i])==int:
##        print(l[i],end=" ")
##        sum+=l[i]
##    i+=1
##print("Sum: ",sum)



'''WAP to extract all the uppercase characters from the string.'''

##s=input("Enter string: ")
##l=""
##i=0
##while i<len(s):
##    if 'A'<=s[i]<='Z':
##        l+=s[i]
##    i+=1
##print("String: ",l)


'''WAP to toggle a string.'''  #toggle means upper to lower alphabet and viceversa

##s=input("Enter string: ")
##i=0
##out=" "
##while i<len(s):
##    if 'A'<=s[i]<='Z':
##        out+=chr(ord(s[i])+32)
##    elif 'a'<=s[i]<='z':
##        out+=chr(ord(s[i])-32)
##    else:
##        out+=s[i]
##    i+=1
##print("Toggled: ",out)



'''WHILE _ INFINITE LOOP'''

'''WAP to take numbers from user until the user enter 0.'''

##while True:
##    n=int(input("Enter number: "))
##    if n==0:
##        print("End!!")
##        break



'''WAP to take username and password from the user ,until the user enters the correct username and password.(Only ask for the password if the username is valid).'''


##user='ritha'
##passw='ritha1234'

##while True:
##    username=input("Enter username : ")
##    if username==user:
##        print("Username Correct")
##        password=input("Enter password: ")
##        if password==passw:
##            print("Password crrect")
##            break
##        else:
##            print("Incorrect password")
##    else:
##        print("Incorrect username")
            





'''WAP to print the index of integers from the list.'''

##l=[1,2,'hi',30.2,(1,2),[3,4],90,234]
##for i in range(len(l)):
##    if type(l[i])==int:
##        print(i,end=" ")



















#NESTED FOR LOOP


n=int(input("Enter number: "))
factsum=0
for j in str(n):
    fact=1
    for i in range(1,int(j)+1):
        fact*=i
    factsum+=fact
if factsum==n:
    print("Strong Number")
else:
    print("Not strong number")
        





























































#WHILE LOOP PRACTICE QSTNS


'''WAP to print multiplication table for n.'''

##n=int(input("Enter number: "))
##i=1
##print("table: ")
##while i<=10:
##    print(n*i)
##    i+=1



'''WAP to find the sum of n natural numbers.'''

##n=int(input("Enter number: "))
##sum=0
##while n>0:
##    sum+=n
##    n-=1
##print("Sum: ",sum)



'''WAP to extract all the lowercase characters present in a string.'''

##s=input("Enter string: ")
##i=0
##out=""
##while i < len(s):
##    if 'a'<=s[i]<='z':
##        out+=s[i]
##    i+=1
##print(out)



'''WAP to extract all the vowels present in a string.'''

##s=input("Enter string:")
##out=''
##i=0
##while i<len(s):
##    if s[i] in 'AEIOUaeiou':
##        out+=s[i]
##    i+=1
##print(out)



'''WAP to print the factors of a integer.'''

##n=int(input("Enter number: "))
##out=''
##i=1
##while i<=n:
##    if n%i==0:
##        print(i)
##    i+=1
    

'''WAP to check whether a number is perfect number or not.'''

##n=int(input("Enter number: "))
##out=0
##i=1
##while i<n:     
##    if n%i==0:
##        out+=i
##    i+=1
##if out==n:
##    print("Perfect number")
##else:
##    print("Not perfect number")



'''WAP to extract all the even integers present in a tuple at odd index.'''

##t=eval(input("Enter values:"))
##out=()
##i=1
##while i<len(t):
##    if type(t[i])== int and t[i]%2==0:
##        print(t[i])
##    i+=2



'''WAP to remove duplicates value from list without converting it into set.'''

##l=eval(input("Enter values: "))
##i=0
##new=[]
##while i < len(l):
##    if l[i] not in new:
##        new.append(l[i])
##    i+=1
##print(new)
##        



'''WAP to find the sum of all the odd numbers between the given range.'''

##r=int(input("Enter range: "))
##ssum=0
##while r>0:
##    if r%2!=0:
##        ssum+=r
##    r-=1
##print(ssum)


##OR

##start=int(input("Enter starting value: "))
##end=int(input("ENTER ENDING VALUE: "))
##
##while start<=end:
##    if start%2!=0:
##        ssum+=start
##    start+=1
##print("Sum of odd numbers: ",ssum)



'''WAP to find the greatest number in a given list of integers.'''

##l=eval(input("Enter integers: "))
##high=l[0]
##i=1
##while i<len(l):
##    if l[i]>high:
##        high=l[i]
##    i+=1
##print("Greatest number: ",high)




'''WAP to login to phonepe by entering correct otp.'''

##import random
##while True:
##    gen_otp=random.randint(1000,9999)
##    print("Otp generated")
##    user_otp=int(input("Enter otp: "))
##    if gen_otp==user_otp:
##        print("Login successfully")
##        break;
##    else:
##        print("Enter proper otp: ")
    



'''WAP to find the sum of cube of individual digit in a string.'''

 
##s=input("enter string: ")
##i=0
##cubesum=0
##while i<len(l):
##    if '0'<=s[i]<='9':
##        cubesum+=int(s[i])**3
##    i+=1
##print("Sum of cube: ",cubesum)



'''WAP to check whether  the number is Armstrong or not.'''

##n=abs(int(input("Enter number: ")))
##temp=n
##ssum=0
##l=len(str(n))
##while n>0:
##    last=n%10
##    ssum+=last**l
##    n//=10
##if temp==ssum:
##    print("Armstrong")
##else:
##    print("Not armstrong")

##OR

##n=abs(int(input("Enter number: ")))
##s=str(n)
##i=0
##Sum=0
##while i <len(s):
##    Sum+=int(s[i])**3
##    i+=1
##if Sum==n:
##    print("Armstrong")
##else:
##    print("Not Armstrong")



# ALT + 3 --> COMMENTING
# ALT + 4 --> UNCOMMENTING



'''1. WAP to add two numbers by taking from users.'''

##a=int(input("Enter first number:"))
##b=int(input("Enter 2nd number:"))
##print("sum: ",a+b)



'''2.WAP to print the square of a number.'''

##a=int(input("Enter the number:"))
##print("square: ",a**2)



'''3.WAP to extract the last character from a string.'''

##s=input('Enter the string: ')
##print("Last character: ",s[-1])



'''4.WAP to reverse a string.'''

##s=input('Enter the string;')
##print("reverse: ",s[::-1])



'''1. WAP to find the area of a rectangle by taking its length and breadth'''

##1
##l=int(input("Enter the length:"))
##b=int(input("Enter the breadth:"))
##print("Area: ",l*b)



'''2. WAP to take the radius of circle, and print its diameter and area.'''

##r=int(input("Enter the radius:"))
##print("Diameter: ",r*2,"Area: ",3.14*(r**2),sep=' ')



'''3. WAP to print half of a number.'''

##a=float(input("Enter the number: "))
##print("Half of a number; ",a/2)



'''4. WAP to take marks of 3 subjects and print the total marks and average marks.'''

##a,b,c=int(input("Enter marks of 3 subjects: "))
##tot=a+b+c
##avg=tot/3
##print("Total: "
'''5. WAP to print the middle character of a string(Consider odd length string.).'''


''' IF '''

'''1.WAP to write a program to check a number is even or not'''

##num=int(input("Enter the number: "))
##if num%2==0:
##      print("Even")


'''2.WAP to check whether a string has exactly 5 characters in it.'''

##s=input("Enter the string:")
##l=len(s)
##if l==5:
##    print("Yes")


'''3.WAP to check whether a number is greater than 200.'''

##num=int(input("Enter a number: "))
##if num>200:
##    print("Yes greater than")


'''4.WAP to print the square of a number only if it is a multiple of 3.'''

##num=int(input("Enter the number: "))
##if num%3==0:
##    print("Square: ",num**2)
    

'''WAP to check whether a number is 2-digit number.'''

##num= int(input("Enter the number: "))
##if 10<=num<=99 or -99<=num<=-10:
##    print("2-digit number")
    


'''WAP to check whether a character is uppercase or not.'''

##c=input("Enter the character: ")
##if 'A'<=c<='Z':
##    print("Uppercase")


'''WAP to check whetehr a character is digit or not.'''

##c=input("Enter the character: ")
##if '0'<=c<='9':
##    print("Digit")


'''1.WAP to check whether a dat is float or not.'''

##data=eval(input("Enter data:"))
##if type(data)==float:
##    print("Float")
##else:
##    print("Not float")


'''2.WAP to check whether a string is palindrome or not.'''

##s=input("Enter string: ")
##reverse=s[::-1]
##if reverse==s:
##    print("Palindrome")
##else:
##    print("Not palindrome")


'''3.WAP to check whether a character is vowel or not.'''

##c=input("Enter character: ")
##vow=['a','e','i','o','u'] #or as a string, vow='aeiouAEIOU
##if c in vow:
##    print('vowel')
##else:
##    print("consonant ")


'''4.WAP to check whether the given data is single value datatype or not.'''

##data=eval(input("Enter data: "))
##single=[int,float,bool,complex]
##if type(data) in single:
##    print("Single value datatype")
##else:
##    print("Not single value datatype")


'''5.WAP to print the square of a number if it is even.'''

##d=int(input("Enter number: "))
##if d%2==0:
##    print("Square: ",d*d)
##else:
##    print("Odd value")


'''6.WAP to print ASCII value of a character only if it is uppercase.'''

##c=input("Enter character: ")
##if 'A'<=c<='Z':
##    print ("ASCII: ",ord('c'))  # ord(variable) is used toget the ASCII value of a character
##else:                           #chr(ASCII value) is used to get the character from ASCII value
##    print("Not uppercase")


'''7.WAP to print the cube of a number only if it is divided by 9 or 6.'''

##num=int(input("Enter number: "))
##if num%6==0 or num%9==0:
##    print("Cube: ", num**3)
##else:
##    print("Not divisible by 9 or 6")


'''8.WAP to check whether the given number is 3-digit  number or not.'''

##num=int(input("nter the number: "))
##if 100<=num<=999:
##    print("3-digit number")
##else:
##    print("Not 3-digit number")


'''9.Wap to check whether the last digit of a given number is 5.'''

##num=int(input("Enter the number: "))
##s=str(num)
##if s[-1]==5:
##    print("Yes last character 5")
##else:
##    print("No")




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

# i=10
# while i<=100:
#     if i%10==0:
#         print(i, end=" ")
#     i+=10

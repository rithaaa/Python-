# PART-1 Questions (1-10)

'''WAP to check whether the given string has an odd length.
*If the length is odd, check whether the middle character is an alphabet.
*If it is an alphabet,print its ASCII value.
*Otherwise print the middle character as it is.
*else print it as even number.'''

##s=input("Enter string: ")
##if len(s)%2!=0:
##    print("Odd")
##    if 'A' <= s[(len(s)-1)//2] <=  'Z' or 'a'<=s[(len(s)-1)//2]<='z':
##        print("ASCII: ",ord(s[(len(s)-1)//2]))
##    else:
##        print("Middle: ", s[(len(s)-1)//2])
##else:
##    print("Even")



'''2. WAP to check whether the first and last elements of a list are integers.
    *If both are integers,Compare them and print the greater value.
    *Otherwise, print"Comparison not possible".'''

##l=eval(input("Enter the list: "))
##if type(l[0]) and type(l[-1])==int:
##    if l[0]>l[-1]:
##        print("Greater: ",l[0])
##    else:
##        print("Greater: ",l[-1])
##else:
##    print("Comparison not possible")


'''3.WAP to check whether a tuple contains exactly three elements.
    *if yes, check whether the first and last elements belong to the same datatype.
    *If they belong to the same type, print "same datatype".
    *Otherwise, print "Different Data types".'''

##t=eval(input("Enter tuple:"))
##if len(t)==3:
##    print("Exactly 3 element")
##    if type(t[0])==type(t[-1]):
##        print("Same datatype")
##    else:
##        print("Different datatype")

'''4.WAP to check whether a character is an alphabet.
    *If yes, check whether it comes before 'n'.
    *If yes, print "First Half Alphabet".
    *Otherwise, print 'second Half alphabet'.
    *If not an alphabet, print 'Invalid character'.'''

##c=eval(input("Enter the character: "))
##if 'A' <=c<= 'Z' or 'a' <= c<= 'z':
##    print("Alphabet")
##    if c<='n':
##        print("First half Alphabet")
##    else:
##        print("Secong half alphabet")
##else:
##    print("Invalid character")


'''5.WAP to check whether a string starts with a lowercase letter.
    *If yes, check whether it ends with an uppercase letter.
    *if both are true, print the reversed string.
    *Otherwise, print the original string. '''

##s=input("Enter the string: ")
##if 'a' <= s[0] <='z':
##    print("Start- lowercase")
##    if "A"<=s[-1]<="Z":
##        print("Reversed: ",s[::-1])
##else:
##    print("OG string: ",s)
        


'''6.WAP to check whether a list contains exactly five elements.
    *If yes, compare the second and fourth elements.
    *print the greater element if both are integers.
    *Otherwise, print 'Invalid comparison'.'''

##l=eval(input("Enter the list: "))
##if len(l)==5:
##    if type(l[1]) and type(l[3])==int:
##        if l[1]>l[3]:
##                print("Greater: ",l[1])
##        else:
##                print("Greater: ",l[3])
##    else:
##        print("Invalid Comparison")
        
    

'''7.WAP to check whether the given integer is divisible by both 4 and 9.
    *If yes,print its square.
    *Else if divisible only by 4, print its cube.
    *Else if divisible only by 9, print half of the number.
    *Otherwise, print the number itself.'''

##a=int(input("Enter the number: "))
##if a%4==0 and a%9==0:
##    print("Square: ",a*a)
##elif a%4==0:
##    print("Cube: ",a**3)
##elif a%9==0:
##    print("Half: ",a//2)
##else:
##    print("OG number: ",a)



'''8. Write a program to check whether two strings have the same first character.
    *If yes, compare their lengths and print the longer string.
    *If both lengths are equal, print "Equal Length".
    *Otherwise, print "Different Starting Characters".'''


##a=input("Enter first string: ")
##b=input("Enter second string: ")
##if a[0]==b[0]:
##    if len(a)>len(b):
##        print("Greatest: ",a)
##    elif len(a)==len(b):
##        print("Equal length")
##    else:
##        print("Greatest: ",b)
##else:
##    print("Different starting characters.")

'''9. Write a program to check whether the middle element of a tuple is a string.
    *If it is a string, check whether it is a palindrome.
    *If yes, print the length of the string.
    *Otherwise,print the reversed string.
    *If it is not a string, print its datatype.'''

##t=eval(input("Enter elements in tuple: "))
##if type(t[(len(t)-1)//2])==str:
##    if t[(len(t)-1)//2]==t[(len(t)-1)//2][::-1]:
##        print("Palindrome")
##        print("Length of the string: ", len(t[(len(t)-1)//2]))
##    else:
##        print("Reversed: ",t[(len(t)-1)//2][::-1])
##else:
##    print("Datatype: ",type(t))
##    


'''10. Create a simple login system using nested if.
    *Verify the username.
    *If correct, verify the password.
    *If correct, ask for "Profile", "Settings", or "Logout".
    *Print the appropriate message.
    *If an invalid option is selected, print "Invalid Choice".'''


##username=input("Enter username: ")
##password=input("Enter password: ")
##
##user_in=input("Username: ")
##pass_in=input("Password: ")
##
##if username==user_in:
##    if password==pass_in:
##        c=input("Enter your choice: Profile, Settings, Logout")
##        if c=='Profile:
##            print("Setup your profile now")
##        elif c=='Settings':
##            print("Going to Setting")
##        elif c=='Logout':
##            print("Logout")
##        else:
##            print("Invalid Choice")
##            

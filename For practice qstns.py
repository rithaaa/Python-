# FOR PRACTICE QSTNS


'''1.WAP to extract all the vowels from a given string.'''

##s=input("Enter string: ")
##for i in s:
##    if i in 'AEIOUaeiou':
##        print(i)
        

'''2.WAP to replace space by underscore in a given string.'''

##s=input("Enter string: ")
##out=''
##for i in s:
##    if i==' ':
##        out+='_'
##    else:
##        out+=i
##print(out)


'''3.WAP to check whether a string is palindrome or not without using slicing.'''

##s=input("Enter string: ")
##out=''
##for i in s:
##    out=i+out
##if s==out:
##    print("Palindrome")
##else:
##    print("Not palindrome")


'''4.WAP to remove duplicate values from a list.'''

##l=eval(input("Enter values: "))
##out=[]
##for i in l:
##    if i not in out:
##        out.append(i)
##print(out)


'''5.input: (12,3.4,'hello',2+3j,'python','bye',False)
output: {'hello':5,'python':6,'bye':3}'''

##d=eval(input("Enter value: "))
##s={}
##for i in d:
##    if type(i)==str:
##        s[i]=len(i)
##print(s)


'''6.output: {'hello':'ho','python':'pn','bye':'be'}'''

##d=eval(input("Enter value: "))
##s={}
##for i in d:
##    if type(i)==str:
##        s[i]=i[0]+i[-1]
##print(s)


'''7. input: 'aPpLe#123'
output: {'a':'A','P':'p','p':'P','L':'l','e':'E'}'''

##d=eval(input("Enter value: "))
##s={}
##for i in d:
##    if 'a'<=i<='z':
##        s[i]=chr(ord(i)-32)
##    elif 'A'<='Z':
##        s[i]=chr(ord(i)+32)
##print(s)



'''8. input: 'hai hello bye'
output: 'bye hello hai'. '''


##s=input("Enter string: ")
##sp=s.split()        #to split the string ito list of items syntax: var.split('char')
##rev=sp[::-1]
##out=' '.join(rev)  #to join items in the list syntax: 'char'.join(var)
##print(out)


'''9. input: hai hello bye
output: iah hello bye'''


##s=input("Enter string: ").split()
##out=[]
##for i in s: 
##    out.append(i[::-1])  
##print(' '.join(out))



#28/07/26


'''1. input: 'Everyone Loves Python'
output: 'Ee Ls Pn'. '''

##s=input("Enter string").split()
##out=[]
##for i in range(len(s)):
##    out.append(s[i][0]+s[i][-1])
##print(' '.join(out))


##OR

##s=input("Enter string").split()
##out=[]
##for i in s:
##    out.append(i[0]+i[-1])
##print(' '.join(out))



'''2. input: 'abcabacbcbc'
output: {'a':3,'b':4,'c':4} '''


##s=input("enter string: ")
##out={}
##for i in s:
##    if i not in out:
##        out[i]=1
##    else:
##        out[i]+=1
##print(out)


'''3. input: 'abcabacbcbc'
output: 'a3b4c4'. '''

##s=input("Enter string: ")
##out=''
##for i in s:
##    if i not in out:
##        out+=i+str(s.count(i))
##print(out)

'''4. WAP to find the divisors or factors of a given number.'''

##s=int(input("Enter number: "))
##out=[]
##for i in range(1,s+1):
##    if s%i==0:
##        out.append(i)
##print(out)




'''Extra qstns'''

'''1.WAP to find the length of homogeneous tuple without len.'''

##t=eval(input("Enter values: "))
##count=0
##for i in t:
##    count+=1
##print(count)

'''2.WAP to extract all even numbers present in a list.'''

##l=eval(input("Enter values: "))
##out=[]
##for i in l:
##    if i%2==0:
##        out.append(i)
##print(out)


'''3.WAP to remove dupplicates from a list.'''

##l=eval(input("Enter values: "))
##out=[]
##for i in l:
##    if i not in out:
##        out.append(i)
##print(out)


'''4.WAP to reverse a string without using slicing.'''

##s=input("Enter string: ")
##out=''
##for i in range(len(s)-1,-1,-1):
##    out+=s[i]
##print(out)
    
'''5.WAP to extract all the lowercase characters in a string only if the ascii value is even.'''

##s=input("Enter string: ")
##out=''
##for i in s:
##    if 'a'<=i<='z':
##        print(ord(i))
##        if ord(i)%2==0:
##            out+=i
##print(out)


'''6.WAP to check whether the last digit of an integer is even or not.'''

##n=int(input("Enter number: "))
##if (n%10)%2==0:
##    print("Even")
##else:
##    print("Odd")


'''7.WAP to extract all the key value pairs from the dictionary only if the keys are if  string datatype  and values are integers.'''

##d=eval(input("Enter value:"))
##out={}
##for i in d:
##    if type(i)==str and type(d[i])==int:
##        out[i]=d[i]
##print(out)

    
    
'''8.WAP to extract key value pairs from the dictionary only if both keys and values ae exactly the same.'''

##d=eval(input("Enter the values: "))
##out={}
##for i in d:
##    if i==d[i]:
##        out[i]=d[i]
##print(out)

'''9. s='power star'
out={"'power": "rewop'", "star'": "'rats"}'''

##d=input("Enter the values: ").split()
##out={}
##for i in d:
##        out[i]=i[::-1]
##print(out)


'''10.s='power star'
out={'power':5,'star':4}'''

##d=input("Enter the values: ").split()
##out={}
##for i in d:
##        out[i]=len(i)
##print(out)


'''11.WAP to extract all the non default values from a list.'''

##l=eval(input("Enter values:"))
##out=[]
##for i in l:
##    if i:
##        out.append(i)
##print(out)


'''12.WAP to check whether the list is homogeneous or not.'''

##l=eval(input("Enter values: "))
##data=l[0]
##for i in l:
##    if type(i)!=type(data):
##        print("Heterogeneous")
##        break
##else:
##    print("Homogeneous")


'''13.Wap to replace the space by * in a string.'''
##s=input("Enter string: ").split()
##print('*'.join(s))

'''14.WAP to count the number of occureence of a specified character.'''

##s=input("Enter string: ")
##c=input("Enter character: ")
##count=0
##for i in s:
##    if c==i:
##        count+=1
##print(count)


'''15.WAp to get the following output.
    s='always keep smiling'
    out-'syawla peek gnilims'.  '''

##s=input("Enter the string: ").split()
##out=[]
##for i in s:
##    out.append(i[::-1])
##print(' '.join(out))



'''16.WAp to get the following output.
        in='push maadi kushi padi'
        out= {'push':'ph','maadi':'a','kushi':'s','padi':'pi'}  '''


##s=input("Enter string: ").split()
##out={}
##for i in s:
##    if len(i)%2==0:
##        out[i]=i[0]+i[-1]
##    else:
##        out[i]=i[len(i)//2]
##print(out)


'''17.WAp to toggle a string.'''


'''18.WAP to extract the upper,lower,digit and special characters present in a string to different output variable.'''

##s=input("Enter string: ")
##u,l,d,c='','','',''
##for i in s:
##    if 'A'<=i<='Z':
##        u+=i
##    elif 'a'<=i<='z':
##        l+=i
##    elif '0'<=i<='9':
##        d+=i
##    else:
##        c+=i
##print(u)
##print(l)
##print(d)
##print(c)


'''19.WAP to get the following output
    s=['jiocinema.com','file.py','web.html','amazon.com','www.org']
    out=['com','py','html','org']  '''

##s=eval(input("Enter values: "))
##out=[]
##o=[]
##for i in s:
##    out=i.split('.')
##        if words[-1] not in o:           
##          o.append(out[-1])
##print(o)

'''20.WAP to get the following output.
    s=['jiocinema.com','file.py','web.html','amazon.com','www.org']
    out={'com':['jiocinema','amazon'],'py':['file','python'],'html':['web'],'org':['www']} '''

##s=eval(input("Enter string: "))
##out={}
##for i in s:
##    words=i.split('.')
##    if words[-1] not in out:
##        out[words[-1]]=[words[0]]
##    else:
##        out[words[-1]].append(words[0])
##print(out)


'''21.WAp to get the following output.
l=['hai',34,3.4,'hello',90,'byebye']
out={'hai':'hi','hello':'ho','byebye':be} '''

##s=eval(input("Enter values: "))
##out={}
##for i in s:
##    if type(i)==str:
##        out[i]=i[0]+i[-1]
##print(out)

'''22. WAP to get the following output.
    In='hello'
    out={0:'h',1:'e',2:'l',3:'l',4:'o'} '''

##s=input("Enter string: ") 
##out={}
##for i in range(len(s)):                  
##    out[i]=s[i]       
##print(out)



'''23.WAP to extract all the string values present in list only if the string is palindrome.'''

##s=eval(input("Enter values: "))
##out=[]
##for i in s:
##    if type(i)==str and i==i[::-1]:
##          out.append(i)
##print(out)

'''24. WAP to return the positions of vowels present in the given string. '''

##s=input("Enter string: ")
##out=[]
##for i in range(len(s)):
##    if s[i] in 'AEIOUaeiou':
##        out.append(i)
##print(out)

'''25. WAP to check whether the given collection is having nested collection or not.'''

##s=eval(input("Enter values: "))
##for i in s:
##    if type(i) in [list,tuple,dict,set,str]:
##        print("Nested Collection")
##        break
##else:
##    print("Doesn't have nested collection")


'''26. WAP to count the number of words in a string.'''

##s=input("Enter string: ").split()
##print (len(s))

#OR

##s=input("Enter string: ").split()
##count=0
##for i in s:
##    count+=1
##print(count)


'''27.WAP to check whether the number is neon number or not.'''

##n=int(input("Enter number: "))
##s=n**2
##out=0
##for i in str(s):
##    out+=int(i)
##if n==out:
##    print("Neon Number")
##else:
##    print("Not Neon")


'''28.WAP to find the longest word in a string.'''

##s=input("Enter string: ").split()
##large=''
##for i in s:
##    if len(i)>len(large):
##        large=i
##print(large)

    
##Next Qstns

'''1.WAP to replace the special character present in a string by space.'''

##s=input("Enter string: ")
##out=''
##for i in s:
##    if 'A'<=i<='Z' or 'a'<=i<='z' or '0'<=i<='9':
##        out+=i
##    else:
##        out+=' '
##print(out)

    
'''2.WAp to print the square of all the integrs present in list.'''

##l=eval(input("Enter values: "))
##for i in l:
##    if type(i)==int:
##        print(i,i**2)


'''3.WAP to extract all the odd numbers present at even index from a list.'''

##l=eval(input("Enter values: "))
##out=[]
##for i in range(len(l)):
##    if l[i]%2!=0 and i%2==0:
##        out.append(l[i])
##print (out)

'''4. WAP to extract all the mutable values present in a tuple.'''

##t=eval(input("Enter values: "))
##out=[]
##for i in t:
##    if type(i) not in [list,set,dict]:
##        out.append(i)
##print(out)

'''5. WAP to get the following output.
In = '10100011231'
Out ='0101110000'
(0 → 1 and 1 → 0, if it is other than 0 & 1 ignore) '''

##s=input("Enter string: ")
##out=''
##for i in s:
##    if i=='0':
##        out+='1'
##    elif i=='1':
##        out+='0'
##print(out)


'''6.WAP to get the following output.

In = 'abacbaacc'
Out = {'a':4, 'b':2, 'c':3} '''

s=input("Enter string: ")
out={}
count=1
for i in range(len(s)):
    if s[i] not in out:
        out[s[i]]=count
else:
    count+=1
    out[s[i]]=count
print(out)

'''7.WAP to extract key-value pair from the dictionary only if the key is Boolean datatype.'''
'''8.WAP to get the following output.

In = '127342'
Out = '242173'
(Extract even and odd digits separately and concatenate both.)'''




























    












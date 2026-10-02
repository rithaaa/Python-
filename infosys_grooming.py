'''Take number from user until we get 0'''

##while True:
##    n=int(input("Enter number: "))
##    if num==0:
##        break;
    



'''PREPINSTA'''


''' 1st monsters problem'''
##
##def monsters():
##    n=int(input())
##    e=int(input())
##    power,bonus=[]
##    for i in range(n):
##        power.append(int(input()))
##    for i in range(n):
##        bonus.append(int(input()))
##    print("Power: ",power)
##    print("Bonus: ",bonus)
##
##
##    a=sorted(zip(power,bonus))
##    count=0
##    for i in a:
##        if i[0]<=e:
##            e+=i[1]
##            count+=1
##        else:
##            return count
##    return count
##        
##print(monsters())   




'''10 --> 1010 then reverse it 0101 --> 5'''
 
n=int(input("Enter number: "))
print(bin(n))
a=bin(n)[2:]
print(bin(n)[2:])

out=''
for i in a:
    if i=='1':
        out+='0'
    else:
        out+='1'
print(out)
number=int(out,2)
print(number)

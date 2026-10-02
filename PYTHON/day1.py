# 1.Write a Python program to find the frequency of each element in a list.

# l=eval(input("Enter the list"))
# a={}
# for i in l:
#     if i not in a:
#         a[i]=1
#     else:
#         a[i]+=1
# print(a)

# 2.Write a Python program to find the first element that appears only once in a list.

# l=eval(input("Enter list:"))    #[1,2,1,2,3,4,4,5,6]
# a={}
# for i in l:
#     if i not in a:
#         a[i]=1
#     else:
#         a[i]+=1
# print(a)
# for i in a:
#     if a[i]==1:
#         print(i)
#         break



# 3.Write a Python program to count how many even and odd numbers are present in a list.

# l=eval(input("Enter list: "))
# a=0
# b=0
# for i in l:
#     if i%2==0:
#         a+=1
#     else:
#         b+=1
# print("EVEN: ",a," ","ODD: ",[1,2,3,4,5,6,7,8,9,10,11,13])


# 4.Write a Python program to move all 0s to the end of the list, while keeping the order of the non-zero elements unchanged.

# l=eval(input("Enter the list: "))
# a=[]
# b=[]
# for i in l:
#     if i==0:
#         a.append(0)
#     else:
#         b.append(i)

# print(b+a)

# 5.Write a Python program to find the second largest number in a list.

# l=eval(input("Enter the list: "))   #[1,2,34,45,40]
# largest=l[0]
# second_largest=l[0]
# for i in l:
#     if i>largest:                       #45>34               
#         second_largest=largest          #s=34
#         largest=i                       #l=45
#     elif i >second_largest:
#         second_largest=i
# print(second_largest)


# 6.Remove duplicates without using set(), preserving the original order.

# lst=eval(input("Enter list: "))
# a=[]
# for i in lst:
#     if i not in a:
#         a.append(i)
# print(a)


# 7.Common elements between two lists.

# l1=eval(input("Enter list1: "))
# l2=eval(input("Enter list2: "))
# a=[]
# for i in l1:
#     for j in l2:
#         if i==j:
#             if i not in a:
#                 a.append(i)
# print(a)


# 8.Write a Python program to reverse a list without using reverse() or [::-1].

# lst=eval(input("Enter list: "))         #[1,2,3,4,5]
# a=[]
# for i in range(-1,-len(lst)-1,-1):         
#     a.append(lst[i])
# print(a)

# 9.Write a Python program to find the missing number from a list containing numbers from 1 to n.

# l=eval(input("Enter list: "))
# a=0
# for i in range(1,len(l)+1):
#     if i not in l:
#         print(i)
            
            
# 10.Check whether a list is a palindrome without using [::-1].

# l=eval(input("Enter: "))
# a=[]
# for i in range(len(l)-1,-1,-1):
#     a.append(l[i])
# if a==l:
#     print("Palindrome")
# else:
#     print("Not palindrome")


# 11. Find two numbers in a list whose sum equals a given target.

# lst=eval(input("Enter values: "))       #[2,3,4,6]   #target=7
# target=int(input("Enter Target: "))
# a=[]
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if target==(lst[i]+lst[j]):
#             print(lst[i],lst[j])

# 12.Move all negative numbers to the beginning of a list while preserving their relative order.

# l=eval(input("Enter: "))
# a=[]
# b=[]
# for i in l:
#     if i<0:
#         a.append(i)
#     else:
#         b.append(i)
# print(a+b)


# Write a Python program to find the maximum difference between any two elements in a list.

# l=eval(input("Enter list: "))           #[10, 3, 7, 2, 15]
# a=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if abs(l[i]-l[j])>a:
#             a=abs(l[i]-l[j])
# print(a)
            
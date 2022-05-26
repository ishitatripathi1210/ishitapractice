# l=list(range(0,5))
# l2=l[-1::-1]
# print(l2)
# print(l)


# l=['m','na','i','ke']
# l1=['y','me','s','lly']
# l3=[]
# for i in range(0,len(l)):
#         l3.append(l[i]+l1[i])
# print(l3)

# l=list(range(0,6))
# l2=[ x*x for x in l]
# print(l2)

# l=['hello ','take ']
# l1=['dear ','sir ']
# l3=[]
# for i in l:
#     for j in l1:
#         l3.append(i+j)
# print(l3)

# l=[10,20,30,40,50]
# l1=[100,200,300,400,500]
# for i,j in zip(l,l1[-1::-1]):
#       print(i,j)

# l=[1,2,3,4,5]
# l.append([5,6,7,8])
# print(l)

# l=[5,20,15,20,25,50,20]
# l3=[]
# for i in l:
#     if l.count(i)==1:
#         l3.append(i)
# print(l3)

# l=[(1,2),(3,4),(5,6)]
# l1=[(7,8),(9,10),(11,12)]
# l3=[]
# for i in range(3):
#     for j in range(2):
#         l3.append((l[i][j],l1[i][j]))
# print(l3)

# l='i am ishita'
# l1=l.split()
# print(l1)

# l=list(input())
# l2=l[::-1]
# length=len(l)
# c=0
# if l==l2:
#     print("palindrome")
# else:
#         print("non palindrome")
# for i,j in zip(l,l2):
#     if i==j:
#         c+=1
#     else:
#         print("not palindrome")
#         break
# if c==length:
#     print('palindrome')


# l=list(input())
# l1=[]
# for i in l:
#     if i==' ':
#        l1.append(i)
#     elif i!=" ":
#         l1.append(chr(ord(i)-32))
# str=""
# for i in l1:
#     str+=i
# print(str)

# str='madam'
# str1=str[ : :-1]
# if(str==str1):
#     print('pallindrome')
# else:
#     print('not pallindrome')    

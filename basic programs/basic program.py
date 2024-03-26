#--------------------------
'''

n=int(input("Enter a number"))
if n==0:
    print("Wrong Input")
else:
    for i in range(n,n+1):
        val=n*(n*1)
        print(val)
'''

#----------------------------------
'''
x=0
str1="thisismycountryindia"
for i in str1:
    x=x+1
    print(str1[0:x])
for i in str1:
    x=x-1
    print(str1[0:x])
'''
#-----------------------
'''

n=int(input("enter a number"))
for i in range(0,n):
     for j in range(0,i+1):
       print("* ",end="")
     print("\r")
'''

#------------------------
'''
a1 = 1045
a3="10100"
a2 = int(format(int(a3,2),'d'))
print(a2)

a4=1045
a5=format(a4,'x')
print(a5)

'''




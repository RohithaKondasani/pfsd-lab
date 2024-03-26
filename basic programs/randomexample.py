import random
n = random.randbytes(1)
print(n)

print(random.randrange(1,10))



print(random.randint(100,211))
mylist = ("jadeja","Ashwin","Rohitha","Shami","dhoni","virat")
mylist1 = {"jadeja","Ashwin","Rohitha","Shami","dhoni","virat"}
mylist2 = ["jadeja","Ashwin","Rohitha","Shami","dhoni","virat"]
print(random.shuffle(mylist2))




import string
import random
S = 10
ran = ''.join(random.sample(string.ascii_uppercase + string.digits,k = S))
s1=4
ran1 = ''.join(random.sample(string.digits,k=6))
print(ran1)

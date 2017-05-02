sums = 8
a = [7, 2, 1, 4, 7, 4, 5, 3]  #sums=8

n = len(a)
result = []
for i in range(0, n):

    for j in range(i+1, n):

        if sums == a[i] + a[j]:
            result.append((a[i], a[j]))
print result


a = sorted(a)

i = 0
j = len(a)-1

print a


result1 =[]

while i < j:

    if a[i] + a[j] == sums:

        result1.append((a[i], a[j]))

    if a[i] + a[j] < sums:
        i += 1
    else:
        j -= 1
    print i,j


print result1


result2=[]

a = [7, 2, 1, 4, 7, 4, 5, 3]
hashmap = {}
for index, value in enumerate(a):
    hashmap[value] = index


for index , value in enumerate(a):
    diff = sums -value
    if hashmap.get(diff,None):
        if hashmap[diff] !=index:
            result2.append((diff, value))



digits=[1000000,2,3]
sums=0
multi=1
for index in reversed(range(0,len(digits))):
      sums= sums + digits[index] *multi;

      multi *=10

print (sums+1)


class Bigint(object):
  
  def __init__(self,value):
    
    self.digits=value
    
  def sums(self):
    
    sumz=0
    multi=1
    result=[]
    
    for index in reversed(range(0,len(self.digits))):
      
       sumz += self.digits[index] *multi
       multi*=10
    result.append(sumz)
    
    return self.__class__(sumz)
  
  def __str__(self):
      return 'Bigint (%d)' % (self.digits)
    
    
    
    

obj=Bigint([1,2,3])

print obj.sums()
    
    
  
  

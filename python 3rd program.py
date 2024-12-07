import math
# read input
L=[]
n=int(input("enter the number of elements:"))
for i in range(n):
      val=int(input("enter element{}:".format(i+1)))
      L.append(val)

# print list details
      print('the length of the list is:',len(L))
      print('list contents',L)

#caluclate mean
mean=sum(L)

#caluclate variance
total=sum((elem-mean)**2 for elem in L)
variance=total/n
#caluclate standard deviation
stddev=math.sqrt(variance)
#print results
print("Mean=",mean)
print("Variance=",variance)
print("standard deviation=",stddev)

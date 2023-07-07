import numpy as np
import matplotlib.pyplot as plt
def mymean(y):
    sum,count=0,0
    for i in y:
        sum=sum+i
        count=count+1
    return sum/count
x=np.array([1,2,3,4,5,6])
y=np.array([6,5,1,3,2,1])
n=len(x)
m=(n*sum(x*y)-sum(x)*sum(y))/(n*sum(x*x)-(sum(x))**2)
c=(sum(y)-m*sum(x))/n
for i in x:
    Y=m*x+c
ym=mymean(y)
sse=sum((y-Y)**2)
sst=sum((y-ym)**2)
r2=1-(sse/sst)
print("r^2 value is ",r2)
if r2>0.9:
    print("Best Fit")
else:
    print("Worst Fit")

plt.plot(x,y,color="red",marker='o',markerfacecolor='w')
plt.plot(x,Y,color="blue",marker='o',markerfacecolor='w')
plt.show()

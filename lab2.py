import numpy as np
import matplotlib.pyplot as plt
def mymean(y):
    sum,count=0,0
    for i in y:
        sum=sum+i
        count=count+1
    return sum/count

def delta:
    
    
x=np.array([1,4.2,2.8,3,1.55])
y=np.array([4,2.55,3.4,5.7,3.2])
n=len(x)
sx=sum(x)
sxx=sum(x*x)
sxxx=sum(x*x*x)
sxxxx=sum(x*x*x*x)
sy=sum(y)
sxy=sum(x*y)
sxxy=sum(x*x*y)

d=delta(np.array([[n,sx,sxx],[sx,sxx,sxxx],[sxx,sxxx,sxxxx]]))
d1=delta(np.array([[sy,sx,sxx],[sxy,sxx,sxxx],[sxxy,sxxx,sxxxx]]))
d2=delta(np.array([[n,y,sxx],[sx,sxy,sxxx],[sxx,sxxy,sxxxx]]))
d3=delta(np.array([[n,sx,y],[sx,sxx,sxy],[sxx,sxxx,sxxy]]))

a=d1/d
b=d2/d
c=d3/d

for i in x:
    Y=a+b*x+c*x*x

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

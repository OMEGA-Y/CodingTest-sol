x,y,w,h = map(int,input().split())

print(min(x,y,abs(x-w),abs(y-h),(x**2+y**2)**0.5,(x**2+(y-h)**2)**0.5,((x-w)**2+y**2)**0.5,((x-w)**2+(y-h)**2)**0.5))
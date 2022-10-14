x1=int(input())
y1=int(input()) 
x2=int(input()) 
y2=int(input())
if x1 > x2 and y1 < y2:
    a = x1 - x2
    b = y2 - y1
else:
    a = x2 - x1
    b = y2 - y1

area = a * b
print(area)

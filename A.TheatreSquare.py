n , m , a = list(map(int , input().split()))
l = n // a 
b = m // a 
if n%a != 0 :
    l += 1
if m%a != 0 :
    b += 1
print(l*b)
n , k = map(int , input().split())
lst = list(map(int , input().split()))
val = lst[k-1]
count = 0
for i in lst :
    if i > 0 and i >= val:
        count += 1
print(count)
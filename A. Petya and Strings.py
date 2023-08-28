s1 = input().lower()
s2 = input().lower()
flag = True
# print(s1 , s2)
for  i in range(len(s1)):
    if s1[i] == s2[i]:
        continue
    elif s1[i] > s2[i]:
        flag = False
        print(1)
        break
    else:
        flag = False
        print(-1)
        break
if flag:
    print(0)
s = input()
if '+' in s :
    s = s.split('+')
    s.sort()
    print("+".join(s))
else:
    print(s)
print(" ".join(input().split()[::2]))


s = [int(i) for i in input().split()]
a = list()
for i in range(1, len(s)):
    if s[i] > s[i - 1]:
        a.append(s[i])
print(" ".join(str(i) for i in a))



l = [int(i) for i in input().split(' ')]

mx = max(l)
mn = min(l)

for i in range(len(l)):
    if l[i] == mx:
        l[i] = mn
    elif l[i] == mn:
        l[i] = mx
print(l)



def f(d, k):
    print(d.get(k))

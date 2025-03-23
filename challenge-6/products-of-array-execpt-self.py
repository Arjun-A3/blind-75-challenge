ls = list(map(int,input().split()))

n = len(ls)

pre = [1] *n
pos = [1] *n

pre[0] = pos[n-1] = 1

for i in range(1,n):
    pre[i] = ls[i-1] * pre[i-1]
for i in range(n-2,-1,-1):
    pos[i] = ls[i+1] * pos[i+1]
for i in range(n):
    ls[i] = pre[i] * pos[i]
print(ls)
ls = list(map(int,input().split()))
t = int(input())


#using hashmap

hm = {}
for i,n in enumerate(ls):
    if (t-n) in hm:
        print ([hm[t-n],i])
    else:
        hm[n] = i

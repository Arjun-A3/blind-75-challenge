list = list(map(int,input().split()))

hs= set()
for i,val in enumerate(list):
    if val in hs:
        print(True)
    else:
        hs.add(val)

print(False)

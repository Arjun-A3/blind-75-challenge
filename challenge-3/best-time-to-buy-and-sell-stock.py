stocks = list(map(int,intpu().split()))

# using sliding window
l = 0
r = 1
ans = 0

while r < len(stocks):
    if stocks[l] < stocks[r] :
        if ans < stocks[r] - stocks[l]:
            ans = stocks[r] - stocks[l]
    else:
        l = r
    r+=1
print (ans)
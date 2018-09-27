"""python program to find valid crosses and dimension of crosses
by Shivam Gupta
Sept 27 2018"""
print ("enter no. of columns and rows required")
n,m = list(map(int,input().split()))
#cchecking constraints value
if n < 2 and n > 105:
    print ("invalid range")
    exit()
elif m < 2 and m > 105:
    print ("invalid range")
    exit()
#get string from the user
else:
    a=[]
    for i in range (0,n):
        x = list(input())
        if len(x) == m:
            a = a + [x]
        else:
            print ("invalid length of string")
    print(*a, sep="\n")
hcount=0 #horizontal counter
vcount=0 #vertical counter
k=1
#pattern matching
for i in range (n):
    for j in range (m):
        if a[i][j] == "s":
            hcount=vcount=1
        while j+k < m:
            if a[i][j+k] == "s":
                hcount += hcount
                k +=k
        while j-k > 0:
            if a[i][j-k] == "s":
                hcount +=hcount
                k +=k
        print (hcount)

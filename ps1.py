"""python program to find valid crosses and dimension of crosses
by Shivam Gupta
Sept 27 2018"""
print ("enter no. of columns and rows required")
n,m = list(map(int,input().split()))

if n < 2 and n > 105:
    print ("invalid range")
elif m < 2 and m > 105:
    print ("invalid range")
else:
    s=0
    a=[]
    for i in range (n):
        s = list + (input())
        a = a + [s]
    print(a[:])

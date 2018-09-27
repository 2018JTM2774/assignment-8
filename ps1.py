"""python program to find valid crosses and dimension of crosses
by Shivam Gupta
Sept 27 2018"""
print ("enter no. of columns and rows required")
n = int(input())
m = int(input())
print (n," ",m)
if n < 2 and n > 105:
    print ("invalid range")
elif m < 2 and m > 105:
    print ("invalid range")
else:
    list = []
    for i in range(n):
        s = list(input())
        list += (s)
    print (list)

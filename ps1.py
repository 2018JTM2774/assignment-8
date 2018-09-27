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
    lst = []
    for i in range (0,m):
        lst.append([])
    for i in range (0,n):
        for j in range (0,m):
            lst[i].append(i+j)
            lst[i][j] = 0
    for i in range (0,n):
        for j in range (0,m):
            print ('entry in row: ',j+1, 'column: ',i+1)
            lst[i][j] = input()
    print (lst)

"""python program for encryption of message
by Shivam Gupta
Sept 27 2018"""
#rotate function
def rotate(m,n):
    copy = list(m)
    for i in range(len(m)):
        if n<0:
            m[i+n] = copy[i]
        else:
            m[i] = copy[i-n]


#Creation of 3 groups
group1="abcdefghi"
group2="jklmnopqr"
group3="stuvwxyz_"

comp1 =[]
comp2 =[]
comp3 =[]
ind1=[]
ind2=[]
ind3=[]

# key value from user
print ("enter values of keys\n")
k1,k2,k3 = list(map(int,input().split()))

# string from user
print ("enter encrypted msg\n")
enc = input()
enc_list = list(enc)
#checking constraints on encrypted msg k1,k2 and k3
if len(enc) < 1 and len(enc) > 150:
    print ("invalid length")
elif k1 < 1 and k1 >150:
    print ("invalid range")
elif k2 < 1 and k2 >150:
    print ("invalid range")
elif k3 < 1 and k3 >150:
    print ("invalid range")
#compare group1 in string and copy similar char into comp1
for i in range(0,len(enc)):
    if enc_list[i] in group1:
        comp1.append(enc_list[i])
        ind1.append(i)
#compare group2 in string and copy similar char into comp2
    elif enc_list[i] in group2:
        comp2.append(enc_list[i])
        ind2.append(i)
# compare group3 in string and copy similar char into comp3
    elif enc_list[i] in group3:
        comp3.append(enc_list[i])
        ind3.append(i)



#rotate comp1,comp2,comp3
rotate(comp1,k1)
rotate(comp2,k2)
rotate(comp3,k3)



# decrypted msg
print ("decrypted msg is:\n")
a=b=c=0
for i in range(0,len(enc)+1):
    if i in ind1:
        enc_list[i]=comp1[a]
        a+=1
    elif i in ind2:
        enc_list[i]=comp2[b]
        b+=1
    elif i in ind3:
        enc_list[i]=comp3[c]
        c+=1

#print(enc_list)

for i in enc_list[:]:
    print (i, end ='')

print(" ")

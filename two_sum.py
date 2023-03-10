ar = [1,2,3,4,5,6]
tr = 9
pos=0
for i in range(0,len(ar)-1):
    if ar[i]+ar[i+pos]==tr:
        print(ar.index(ar[i]))
        print(ar.index(ar[i+1]))
        pos= pos+1

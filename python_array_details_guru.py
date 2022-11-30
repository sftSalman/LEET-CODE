import array
balance = array.array('i',[300,200,100,30,22,2,2])
print(balance[1:3])

# inserting element

balance.insert(3,999)

# modifying array


balance[3]=1111
print(balance[3])

# pop element in the array

balance.pop(3)
print(balance)


# delete the element from array
# I just added the commit
balance.remove(2)
print(balance)

# searhing from array

print(balance.index(30))

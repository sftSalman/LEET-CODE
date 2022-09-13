import array
balance = array.array('i', [300,200,100])
print(balance[1])
balance.insert(3,10)
print(balance)
balance.remove(10)
print(balance)
print(balance.index(200))
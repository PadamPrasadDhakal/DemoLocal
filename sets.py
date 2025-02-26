a={1,2,3,4,1,5}    #repetaton doesnot allowed in sets in dictnary it is alowed
print(a)
print(type(a))
# b={}    this will create and empty dictonary not empty set
# adding values to existing sets
a.add(44)
a.add(99)
print(a)
a.add((10,20,30))      #we can add tuple like this but we cannot add list like a.add([10,20,20]), cannot add dictnary alsop
print(a)
print("The length of the set is ",len(a))
# a.remove(20)  it gives error if value doesnt present in the set, discard le chai error didaina
# print("after removel of 20 ",a)
x=a.pop()
print("poped ",x)
print(a)
# clear le chai sabai value haru lai remove garxa empty banauxa, del setNAme le chai set nai udauxa
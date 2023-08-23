#Dictionary
#No substring, no indexing

#keys()
# update()
#pop()
# clear()
# copy()
# fromkeys()
# items()

dfriends ={1:"Ross",2:"Racheal",3:"Phoebie"}
dfriends[4] = "Monica"
print(dfriends)

print(dfriends.get(1))

dfriends.update({5:"Joe"}) #to add new element
print(dfriends)

#removing
dfriends.pop(1)
print(dfriends)

dfriends.popitem()
print("qqqqqqqqq")
print(dfriends)

print("qqqqqqqqq")
print(dfriends.items())


#same value for all the keys
mykeys = (1,2,3,4)
myvalues = ["MDS","Stats"]
x = dict.fromkeys(mykeys,myvalues)
print(x)

DS = {}.fromkeys(['PDS','DBT','Python'],0)  #value of keys:'PDS','DBT','Python'     Values:0
print(DS)


DS['DBT'] = "Sr. Sri"
DS['Python'] = "Dr. Salma"
for i in DS.items():
    print(i)
for i in DS.values():
    print(i)

#Dictonary COmprehesnion
# cubes ={}
cubes = {x: x*x*x for i in range(2,7)}
print(cubes)


key_max = max(zip(cubes.values(),cubes.keys()))



import pandas as pd
#import matplotlib.pyplot as plt
#df = pd.read_csv('HW6Plots.csv')
#print(df)
print("The data is correct")
print("hsh")

# name = input("What is your name?")
# print(name)

# listvar = [1,2,name]
# index2 = listvar[2]
# print(index2)

list = [1,2,3,4,5,6]
list.pop(-2)
print(list)

del list[0:2]
print(list)

newlist =list[1:2] #stops at element 2, does not grab element 2 
print(newlist)

list2 = [0,1,2,3]
#does not seperate elements from list2, groups into 1 element
# newlist.insert(0,list2) 
# print(newlist)
# print(newlist[0])

#use this method instead to add a list to a list
newlist[0:0] = list2
print(newlist)

#extracting specific components of list
import numpy as np
a = np.array([10, 11, 12, 13, 14, 15])
s = [1, 2, 5] 
b = a[s]
print(b)
#b = ([11, 12, 15])

###Dictionaries
## Insertion
emptyvar = {}
emptyvar[25] = "SQUARE OF 5"
print(emptyvar)

##Lookup
dictVar = {"Pi": 3.14, "The square of 5":25, "The square of 6":36}
#Keys, values, and items
dictkeys = dictVar.keys()
dictvalues = dictVar.values()
items = dictVar.items()
print(dictkeys)
print(dictvalues)
print(items)

#all of these return dictionary objects

#Keys, values and items as lists
#list(dictkeys)
temp = []
dictlist1 = []
formatdictlist1 = []
formatdictlist2 = []
dictlist2 = [ [k,v] for k,v in dictVar.items()]
print(dictlist2)


for key, value in dictVar.items():   #dict.items converts dictionary objects into list objects
    temp = [key,value]
    dictlist1.append(temp)

formatdictlist1.extend(dictlist1)
print(dictlist1)
print(formatdictlist1)
print(formatdictlist1[0])
#puts l = [k1,v1,...,kn,vn]
l = []
m = []
c = dictVar.items()
print(c)

##Creates a matrix of the dictionary keys
n = []
for y in dictkeys:   
    print(y)              #x does not need to be defined beforehand, prints tuple from each key-value pair
    n.append(y)            
print(n)

##Creates a matrix of the dictionary values
o = []
for z in dictvalues:
    print(z)
    o.append(z)
print(o)

#extend versus append 
##Creates a matrix of all dictionary keys and values
for x in c:   
    print(x)             
    l.extend(x)          #extend adds iterables (objects such as tuples, strings, lists, sets) to list
    m.append(x)          
print(l) 
print(m)

#for x in c:                 #x does not need to be defined beforehand
    #if x == 3.14:
        #break
    #print(x)             #extend adds iterables (objects in )
#print(l)

#method: index 1 is [k1,v1]
for onekey in dictVar.keys():
    print("key " + str(onekey) + ":," + "value = " + str(dictVar[onekey]))

somestring = "This is a random string"
print(somestring[:5])
print(somestring.count("random"))  #counts amount of times the string is there
print(somestring.index("random")) #index returns the first location which this appears
print(somestring.lower()) #converts string to lowercase
print(somestring.upper()) #converts string to uppercase
print(somestring.split()) #splits into multiple substrings
print(somestring.startswith("random"))
print(somestring.endswith("string"))
print(somestring[-3:]) #counts from the end of the string









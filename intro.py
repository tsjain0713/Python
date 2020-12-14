
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

#Dictionaries
#Insertion
emptyvar = {}
emptyvar[25] = "SQUARE OF 5"
print(emptyvar)

#Lookup
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

for key, value in dictVar.items():   #dict.items converts dictionary objects into list objects
    temp = [key,value]
    dictlist1.append(temp)
formatdictlist1.extend(dictlist1)
print(dictlist1)
print(dictlist2)





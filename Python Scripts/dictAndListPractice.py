def getFirstTwo(mylist):
    return mylist[0:2]

def printFirst(mystring, x):
    new_string = mystring[:x]
    return new_string

def getLastTwo(mylist):
    return mylist[-2:]

def addToEnd(mylist, num1):
    return mylist.append(num1)

def addToFront(mylist, num1):
    return mylist.insert(0, num1)

def getFirstTwoAndLastTwo(mylist):
    new_list = mylist[:2] + mylist[-2:]
    return new_list

def removeFirst(mylist):
    mylist.pop(0)
    return mylist

def removeThird(mylist):
    mylist.pop(2)
    return mylist

def sortList(mylist, ascending):
    if ascending == True:
        return sorted(mylist)
    else:
        return reversed(sorted(mylist))
    
def createDict(list1, list2):
    new_dict = {}
    for i in range(len(list1)):
        new_dict[i] = list2[i]
    return new_dict

def findDictItem(mydict, key):
    if key in mydict:
        return mydict[key]
    
def removeDictItem(mydict, key):
    if key in mydict:
        del mydict[key]
    return mydict

def printDict(mydict):
    for key, value in mydict.items():
        print(f'{key}={value}',end='\n')

newdict = {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}

printDict(newdict)
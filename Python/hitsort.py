#################################################################### supporting functions 
    
def getminimum(array):
    sqrt=isqrt(len(array))
    mini=[]
    for i in range(0,len(array),sqrt):
        mini.append(minimum(array[i:i+sqrt]))
    return minimum(mini)
           
 
def minimum(array):
    if array:
        minValue = array[0]
        for i in range(1, len(array)):
            if array[i] < minValue:
                minValue = array[i]
        return minValue

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

############################################################# Actual functionality here 
def doHit(array,length):
    hit=[]
    heads=[]
    [hit.append([]) for i in range(0,9)]
    for i in range(0,length):
        j=(array[i])%9;
        hit[j].append(array[i])
    for i in range(0,9):
        heads.append(getminimum(hit[i]))
    return hit,heads

def getHead(heads,hit):
    if heads:       
        lat=min(heads)%9
        if hit[lat]:
            insert=min(hit[lat])
            hit[lat].pop(0)
            heads.remove(insert)
            if hit[lat]: 
                heads.insert(lat,getminimum(hit[lat]))
            return insert
        
def doSort(array):
    length=len(array)
    if(length>50):
        hit,heads=doHit(array,length)
        newArray=[]
        while length>0:
            newArray.append(getHead(heads,hit))
            length-=1
        return newArray
    else:
	raise MyError("Can't be used for smaller arrays use array.sort() to get faster results")

        
        
'''
My sort
'''
___AUTHOR___="Hithesh Viswanath"






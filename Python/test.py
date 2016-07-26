#################################################################### supporting functions 
    
def getminimum(array):
    sqrt=isqrt(1000)
    mini=[]
    for i in range(0,len(array),sqrt):
        mini.append(minimum(array[i:i+sqrt]))
    return minimum(mini)
           
 
def minimum(array):
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
        
def mysort(array):
    length=len(array)
    hit,heads=doHit(array,length)
    newArray=[]
    while length>0:
        newArray.append(getHead(heads,hit))
        length-=1
    return newArray
'''
My sort
'''
##############################################################  for comparision
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist
################################################################# for readability
def test(name,function,array):
    start_time = time.time()
    function(array)
    timeTaken=time.time() - start_time
    print("--- %s seconds in %s sort---" % (timeTaken,name))
    return timeTaken
def compare(function1,name1,function2,name2,array):
    times=test(name1,function1,array)/test(name2,function2,array)
    print("--- %s is %s times faster than %s" %(name2,times,name1))
    return times
#################################################################### MAIN
def main(i):
	array=[random.randint(1,10000) for _ in range(i)]
	return compare(bubbleSort,"Bubble Sort",mysort,"My sort",array)
    

####################################################################


import random
import time
t=[]
for i in range(1,4):
    t.append(main(10000))
print t
print "Average times faster is "
print sum(t)/len(t)




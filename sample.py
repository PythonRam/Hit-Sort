import hitsort
import random
array=[random.randint(0,1000) for i in range(0,75)]
array1=array
array1.sort()
if(hitsort.doSort(array)==array1):
	print "Works bitch"


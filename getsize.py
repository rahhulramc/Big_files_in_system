
import os
from os.path import join, getsize
i=0;
arr=[("?",-1.0)]
gpath=os.environ['HOME']
def myfn(a):
	return  a[1];
def gts(gpath):
	for root, dirs, files in os.walk(gpath):
		for name in files:
			try:
				temp = getsize(join(root,name))
			except OSError:
				continue
			path=join(root,name)
			arr.append((path,temp))
			arr.sort(key=myfn)
			if(len(arr)>11):
				arr.remove(arr[1])
	arr.remove(arr[0])
gts(gpath)	
for i in arr:
	print i[0],float(i[1])/float(1000*1000)	
	

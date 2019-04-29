import matplotlib.pyplot as plt
import pylint

xy=open("xy.coordinates",'r')
pointsdic={}
# seperate data into items
pointslist = xy.read()
pointslist=pointslist.replace('\n',',')
pointslist=pointslist.split(',')
for i in range(0,len(pointslist)):
    if i%3 == 0:
        temp=pointslist[i]
    elif i%3 == 1:    
        x=pointslist[i]
    else:   # y
        pointsdic[temp]=(float(x),float(pointslist[i])
print(pointsdic)      


close(xy)
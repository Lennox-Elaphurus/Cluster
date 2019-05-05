import matplotlib.pyplot as plt


xy = open("input.txt", 'r')
pointsdic = {}
# separate data into items
pointslist = xy.read()
pointslist = pointslist.replace('\n', ',')
pointslist = pointslist.split(',')
for i in range(0, len(pointslist)):
    if i % 3 == 0:
        temp = pointslist[i]
    elif i % 3 == 1:
        x = pointslist[i]
    else:   # y
        pointsdic[temp] = (float(x), float(pointslist[i]))
# print(pointsdic)
# input finished
class vertex :
    def __init__(self,name,x,y):
        self.name=name
        self.x=x
        self.y=y
        self.weight=0
        self.arrived=0
        self.neighbors=[]

global total
total = 1000
global V
V=[]
global ANS
ANS={}
global maxdis
maxdis=0
global lowerlimit
lowerlimit=0

def Distance (a, b):
    return ((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y))**(0.5)

def Read ():
    global V
    global maxdis
    for key,value in pointsdic.items():
        V.append(vertex(key, value[0], value[1]))
    for p1 in V:
        for p2 in V:
            tempdis = Distance(p1,p2)
            if tempdis > maxdis:
                maxdis=tempdis
    print("Import ",len(V)," points from input.txt.")

def Init():
    global V
    for p in V:
        p.neighbors.clear()
        p.weight = 0
        p.arrived = False

def AddEdges(radius):
    global V
    for p1 in V:
        for p2 in V:
            if p1!=p2 and Distance(p1,p2) < 2 * radius:
                p1.neighbors.append(p2)
                p2.neighbors.append(p1)
                p1.weight=p1.weight+1
                p2.weight=p2.weight+1

def CountWeights():
    global V
    sum=0
    global lowerlimit
    for p in V:
        sum =sum + p.weight
    average = sum / len(V)
    variance = 0
    for p in V:
        variance = variance+(p.weight - average) * (p.weight - average) / len(V)
    lowerlimit = average - (variance)**(0.5)

def DFS(p1,output):
    global lowerlimit
    if output is True:
        print(p1.name)
    p1.arrived=True
    # print(p1.name,".arrived=True")
    for p2 in p1.neighbors:
        if (not p2.arrived) and p1.weight + p2.weight > 2 * lowerlimit:
            DFS(p2,output)

import random as ra
def printPoint(p):  # for debug
    check=ra.randint(0,1000)
    if(check<5):
        print("p:",p)
        print("p.name:",p.name,"\np.x:",p.x,"\np.y:",p.y,"\np.weight:",p.weight,"\np.arrived:",p.arrived,"\np.neighbors:",p.neighbors)

def Cluster(radius,output):
    global V
    global ANS
    Init()
    AddEdges(radius)
    CountWeights()
    categories = 0
    for p in V:
        # printPoint(p)
        # print("p.arrived:",p.arrived)
        if p.arrived is False:
            categories = categories+1
            if output is True:
                print("Class",categories,":",end="")
            DFS(p,output)
            if output is True:
                print("")
    # print("categories: ",categories)
    # print("len(V) / 3:",len(V) / 3)
    if categories >= 2 and categories <= len(V) / 3:
    # if categories >= 2 :
        if not (categories in ANS):
            ANS[categories] = radius
            print("categories:",categories,"radius:",radius)

# main
Read()
for i in range(1,total+1):
    Cluster(maxdis / 2 / total * i, False)
print("There are ",len(ANS)," methods to cluster.")
print("NO.\tcluster\tradius")
num=0
for key,value in ANS.items():
    num=num+1
    print('%-8d' % num,'%-6d' % key,'%f' % value)
num=input("Please enter the number of method(NO.) you want:")
print("\nThe method you want is as follow:")
for value in ANS.values():
    Cluster(value,True)


xy.close()
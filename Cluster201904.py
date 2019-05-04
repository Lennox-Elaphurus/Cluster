import matplotlib.pyplot as plt


xy = open("xy.coordinates", 'r')
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
print(pointsdic)
# input finished
class vertex :
    def __init__(self,name,x,y):
        self.name=name
        self.x=x
        self.y=y
        self.weight=0
        self.arrive=0
        self.neighbors=[]

total = 1000
V=[]
ANS={}
maxdis=0
lowerlimit=0

def Distance (a, b):
    return ((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y))**(0.5)

def Read ():
    for key,value in pointsdic.items():
        V.append(vertex(key, value[0], value[1]))
    for p1 in V:
        for p2 in V:
            tempdis = Distance(p1,p2)
            if tempdis > maxdis:
                maxdis=tempdis
    print("Import ",len(V)," points from xy.coordinates.")

def Init():
    for p in V:
        p.neighbors.clear()
        p.weight = 0
        p.arrived = False

def AddEdges(radius):
    for p1 in V:
        for p2 in V:
            if p1!=p2 and Distance(p1,p2) < 2 * radius:
                p1.neighbors.append(p2)
                p2.neighbors.append(p1)
                p1.weight=p1.weight+1
                p2.weight=p2.weight+1

def CountWeights():
    sum=0
    for p in V:
        sum =sum + p.weight
    average = sum / len(V)
    variance = 0
    for p in V:
        variance = variance+(p.weight - average) * (p.weight - average) / len(V)
    lowerlimit = average - (variance)**(0.5)
    return lowerlimit
def DFS(p1,output):
    if output is True:
        print(p1.name)
    p1.arrived=True
    for p2 in p1.neighbors:
        if (not p2.arrived) and p1.weight + p2.weight > 2 * lowerlimit is True:
            DFS(p2,output)

def Cluster(radius,output):
    Init()
    AddEdges(radius)
    CountWeights()
    categories = 0
    for p in V:
        if p.arrived is False:
            categories = categories+1
            if output is True:
                print("Class ",categories," :",ending="")
            DFS(p,output)
            if output is True:
                print("")
    if 2 <= categories  and categories <= len(V) / 3:
        if ANS.find(categories) == ANS.end():# debug
            ANS[categories] = radius



xy.close()
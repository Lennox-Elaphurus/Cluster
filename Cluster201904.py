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
class vertex {
    char name[100];
    double x, y;
    vector<vertex*> neighbors;
    int weight;
    bool arrived;

    vertex (char *name_, double x_, double y_) {
        strcpy(name, name_);
        x = x_; y = y_;
    }
};

define Distance (vertex a, vertex b) {
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y))
xy.close()
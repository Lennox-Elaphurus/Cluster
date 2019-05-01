#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

struct vertex {
    char name[100];
    double x, y;
    vector<vertex*> neighbors;
    int weight;
    bool arrived;

    vertex (char *name_, double x_, double y_) {
        strcpy(name, name_);
        x = x_;
        y = y_;
    }
};

const int total = 1000;
double maxdis, lowerlimit;
vector<vertex> V;
map<int, double> ANS;

double Distance (vertex a, vertex b) {
    return sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y));
}

void Read (void) {
    char name[100]; double x, y;
    FILE *fin = fopen("input.txt", "r");
    while (true) {
        int flag = fscanf(fin, "%[^,]%*c%lf%*c%lf\n", name, &x, &y);
        if (flag == EOF) break;
        V.push_back(vertex(name, x, y));
    }
    fclose(fin);
    maxdis = 0;
    for (auto &v1 : V)
        for (auto &v2 : V)
            maxdis = max(Distance(v1, v2), maxdis);
    printf("已从 input.txt 读取 %d 个数据点\n", V.size());
}

void Init (void) {
    for (auto &v : V) {
        v.neighbors.clear();
        v.weight = 0;
        v.arrived = false;
    }
}

void AddEdges (double radius) {
    for (auto &v1 : V)
        for (auto &v2 : V)
            if (&v1 != &v2 && Distance(v1, v2) < 2 * radius) {
                v1.neighbors.push_back(&v2);
                v2.neighbors.push_back(&v1);
                v1.weight++;
                v2.weight++;
            }
}

void CountWeights (void) {
    double sum = 0;
    for (auto &v : V)
        sum += v.weight;
    double average = sum / V.size();
    double variance = 0;
    for (auto &v : V)
        variance += (v.weight - average) * (v.weight - average) / V.size();
    lowerlimit = average - sqrt(variance);
}

void DFS (vertex *v1, bool output) {
    if (output) printf("%s  ", v1->name);
    v1->arrived = true;
    for (auto &v2 : v1->neighbors)
        if (!v2->arrived && v1->weight + v2->weight > 2 * lowerlimit)
            DFS(v2, output);
}

void Cluster (double radius, bool output) {
    Init();
    AddEdges(radius);
    CountWeights();
    int categories = 0;
    for (auto &v : V)
        if (!v.arrived) {
            ++categories;
            if (output) printf("第 %d 类：", categories);
            DFS(&v, output);
            if (output) printf("\n");
        }
    if(2 <= categories  && categories <= V.size() / 3)
        if(ANS.find(categories) == ANS.end())
            ANS[categories] = radius;
}

int main (void) {
    Read();
    for (int i = 1; i <= total; i++)
        Cluster(maxdis / 2 / total * i, false);
    printf("以下为您提供 %d 种聚类方案：\n\n", ANS.size());
    printf("方案编号  聚类数  半径取值\n");
    int num = 0;
    for (auto &ans : ANS)
        printf("%-8d  %-6d  %f\n", ++num, ans.first, ans.second);
    printf("\n请输入您想要的方案编号：");
    scanf("%d", &num);
    printf("\n该聚类方案如下：\n");
    map<int, double>::iterator it = ANS.begin();
    while (--num) it++;
    Cluster(it->second, true);
    return 0;
}

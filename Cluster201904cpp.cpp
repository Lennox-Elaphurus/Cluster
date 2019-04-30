#include <algorithm>
#include <cstdio>
#include <vector>
#include <cstring>
#include <cmath>
using namespace std;

struct vertex {
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

const int total = 10;
double maxdis, radius;
int categories;
vector<vertex> V;

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
    for (auto v1 : V)
        for (auto v2 : V)
            maxdis = max(Distance(v1, v2), maxdis);
    printf("已从 input.txt 读取 %d 个数据点，以下为您提供 %d 种聚类方案：\n\n", V.size(), total);
    printf("方案编号  聚类数  半径取值\n");
}

void Init (void) {
    for (auto &v : V) {
        v.neighbors.clear();
        v.weight = 0;
        v.arrived = false;
    }
    categories = 0;
}

void AddEdges (void) {
    for (auto &v1 : V)
        for (auto &v2 : V)
            if (&v1 != &v2 && Distance(v1, v2) < 2 * radius) {
                v1.neighbors.push_back(&v2);
                v2.neighbors.push_back(&v1);
                v1.weight++;
                v2.weight++;
            }
}

void DFS (vertex *v1, bool output) {
    if (output) printf("%s  ", v1->name);
    v1->arrived = true;
    for (auto &v2 : v1->neighbors)
        if (!v2->arrived)
            DFS(v2, output);
}

int main (void) {
    Read();

    for (int i = 1; i <= total; i++) {
        Init();
        radius = maxdis / 5 / total * i;
        AddEdges();
        for (auto v : V)
            if (!v.arrived) {
                DFS(&v, false);
                categories++;
            }
        printf("%-8d  %-6d  %f\n", i, categories, radius);
    }

    int num;
    printf("\n请输入您想要的方案编号：");
    scanf("%d", &num);
    printf("\n该聚类方案如下：\n");
    Init();
    radius = maxdis / 5 / total * num;
    AddEdges();
    for (auto &v : V)
        if (!v.arrived) {
            printf("第 %d 类：", ++categories);
            DFS(&v, true);
            printf("\n");
        }
    return 0;
}

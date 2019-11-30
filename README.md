# Cluster

## Function

* cluster the points in the file xy.coordinates by Euclid Distance
* plot the result in different class using different color

## Principle

Graph theory:

1. connect the points within different radius
2. count the Connected Components in the graph
3. find the proper radius by comparing the radius of each clusters

## Disadvantage

* Only support plotting the clusters <=8
*for there are only 8 colors in matplotlib.pyplot.scatter()*
* Need to input which method you want according to radius
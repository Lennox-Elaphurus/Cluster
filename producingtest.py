import random as ra


# print(ra.randint(0,100))
output=open("test.txt",'w')
# print(type(output))
for i in range(0,20):
    output.write(str(i)+","+str(ra.randint(0,10))+","+str(ra.randint(0,10))+"\n")
for i in range(20,40):
    output.write(str(i)+","+str(ra.randint(15,30))+","+str(ra.randint(15,30))+"\n")
for i in range(40,80):
    output.write(str(i)+","+str(30)+","+str(ra.randint(30,70))+"\n")
output.close()
print("Instance constructed.")
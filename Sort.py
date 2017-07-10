#метод пузырька
from random import randint

list = [randint(75,200) for i in range(15)]

print(list)

for i in range(len(list),0,-1):
    for j in range(0,len(list)-1):
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]

print(list)






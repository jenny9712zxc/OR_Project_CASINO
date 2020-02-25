import numpy as np
import matplotlib.pyplot as plt

one_p = np.array([
        #    0,    1,    2,    3,    4,    5,    6,    7,    8,    9,   10,   11,   12,   13,   14,   15,   16,   17,   18,   19,   20    21   22     23    24    25    26    27    28    29    30
        [    1,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38,    0],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,20/38,    0,    0,    0,18/38],
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0], 
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    1],
        ])
ob = np.array(one_p)
one_init = np.array([
        [    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    1,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0],])
ob = one_p.dot(one_p)
ob = ob.dot(ob)
ob = one_p.dot(ob)
ob = ob.dot(ob)
ob = ob.dot(ob)
ob = one_init.dot(ob)
expected = 0
print("even & odd/red & black/low & high")
print(ob[0])
for index in range(len(ob[0])):
    expected += ob[0][index]*index

print("even & odd/red & black/low & high expected value")
print("E(x) :\n     ",expected)

xlabel = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
plt.bar(xlabel,ob[0])
plt.show()
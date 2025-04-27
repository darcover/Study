import numpy as np


f = open('matrix.txt','w')
txt='''3,4,17,-3
5,11,-1,6
0,2,-5,8
'''
f.write(txt)
f.close()


mat = np.loadtxt('matrix.txt',delimiter=',')

print(mat.sum())
print(mat.max())
print(mat.min())
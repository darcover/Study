import numpy as np

x=np.array([6,2,0,3,0,0,5,7,0])

idx=np.where(x[:-1]==0)[0]+1
res=x[idx]
print(res.max())
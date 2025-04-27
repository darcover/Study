import numpy as np

def run_length_encode(x):

    values= []
    counts=[]
    if len(x)==0:

        return np.array([]),np.array([])

    current=x[0]
    cnt=1

    for v in x[1:]:
        if v==current:

            cnt+=1
        else:

            values.append(current)
            counts.append(cnt)

            current=v
            cnt=1

    values.append(current)
    counts.append(cnt)
    return np.array(values),np.array(counts)

x=np.array([2,2,2,3,3,3,5])

vals,cnts=run_length_encode(x)
print(vals)
print(cnts)
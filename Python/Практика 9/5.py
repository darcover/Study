import numpy as np
import time

from scipy.stats import multivariate_normal

def logpdf_multivar(X,m,C):

    N,D=X.shape
    C_inv=np.linalg.inv(C)
    det_C=np.linalg.det(C)

    log_const=-0.5*(D*np.log(2*np.pi)+np.log(det_C))
    logs=[]

    for x in X:

        diff=x-m
        logs.append(log_const-0.5*diff.T.dot(C_inv).dot(diff))

    return np.array(logs)

X=np.random.randn(1000,3)

mean=np.zeros(3)
cov=np.eye(3)

start=time.time()

our=logpdf_multivar(X,mean,cov)
print(time.time()-start)

start=time.time()

their=multivariate_normal(mean=mean,cov=cov).logpdf(X)
print(time.time()-start)

print(np.max(np.abs(our-their)))
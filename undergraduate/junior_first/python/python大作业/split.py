import numpy as np
#import pandas as pd 
from sklearn.model_selection import train_test_split

data = np.loadtxt('data.txt',dtype=str)
#print(data.shape)
#print(data[1:10])
x , y = data[:,:3],data[:,3]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)
print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)
#print(x_train[:10])
# #print(y_test[:10])
#np.savetxt('train.txt',np.hstack((x_train,y_train.reshape(8000,1))),fmt = "%s %s %s %s")
np.savetxt('x_train.txt',x_train,fmt='%s %s %s')
np.savetxt('y_train.txt',y_train.astype(int),fmt='%d')
x_validation,x_test,y_validation,y_test = train_test_split(x_test,y_test.reshape(-1,1),test_size = 0.5)
np.savetxt('x_validation.txt',x_validation,fmt='%s %s %s')
np.savetxt('y_validation.txt',y_validation.astype(int),fmt='%d')
np.savetxt('x_test.txt',x_test,fmt='%s %s %s')
np.savetxt('y_test.txt',y_test.astype(int),fmt='%d')
import numpy as np
# 逻辑回归
from sklearn.linear_model import LogisticRegression
# 支持向量机
from sklearn.svm import SVC
# 多层感知机
from sklearn.neural_network import MLPClassifier
# 贝叶斯
from sklearn.naive_bayes import GaussianNB

def accuracy(predicted,y):
    res = predicted == y
    accu = np.mean(res)
    size = len(predicted)
    print('Accuracy of the network on the %d test : %d %%' %(size,100 * accu))

def logisticregression(X,Y,XValidation,YValidation):
    lr = LogisticRegression().fit(X, Y)

    y_pred = lr.predict(XValidation)
    accuracy(y_pred,YValidation)

def svm(X,Y,XValidation,YValidation):
    svc = SVC(kernel='linear').fit(X, Y)
    y_pred = svc.predict(XValidation)
    accuracy(y_pred,YValidation)

def mlp(X,Y,XValidation,YValidation,para1,para2):
    mlp = MLPClassifier(hidden_layer_sizes=(para1, para2,)).fit(X, Y)

    #y_pred = mlp.predict(XValidation)
    #accuracy(y_pred,YValidation)

    train_pred = mlp.predict(X)
    accuracy(train_pred,Y)
    y_pred = mlp.predict(XValidation)
    accuracy(y_pred,YValidation)
    #y_pred = mlp.predict(XValidation)
    #accuracy(y_pred,YValidation)

def bayes(X,Y,XValidation,YValidation):
    mb = GaussianNB().fit(X, Y)

    y_pred = mb.predict(XValidation)
    accuracy(y_pred,YValidation)

if __name__ == '__main__':
    x_train = np.loadtxt('final_train.txt', dtype=float)
    y_train = np.loadtxt('y_train.txt', dtype=float)
    x_validation = np.loadtxt('final_validation.txt', dtype=float)
    y_validation = np.loadtxt('y_validation.txt', dtype=float)
    x_test = np.loadtxt('final_test.txt', dtype=float)
    y_test = np.loadtxt('y_test.txt', dtype=float)
    x_train[:,12],x_validation[:,12],x_test[:,12] = -x_train[:,12],x_validation[:,12],x_test[:,12]
    # print('logistic regression:')
    # logisticregression(x_train,y_train,x_validation,y_validation)
    print('svm')
    svm(x_train,y_train,x_validation,y_validation)
    # print('mlp:')
    # for para1 in range(20,200,5):
    #     for para2 in range(20,200,10):
    #         print('the hidden layers for parameters para1: %d para2: %d' %(para1,para2))
    #         mlp(x_train,y_train,x_validation,y_validation,para1,para2)
    # print('bayes')
    # bayes(x_train,y_train,x_validation,y_validation)
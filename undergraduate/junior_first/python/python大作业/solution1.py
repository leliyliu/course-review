import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

def train(x_train,y_train):
    svm_clf = Pipeline((
    ("scaler", StandardScaler()),
    ("linear_svc", LinearSVC(C=1, loss="hinge")),
    ))
    svm_clf.fit(x_train, y_train)
    return svm_clf

def validation(predictor,x_validation,y_validation):
    validate = predictor.predict(x_validation) == y_validation
    size = len(y_validation)
    accu = np.sum(validate == True)/size
    print('Accuracy of the network on the %d test : %d %%' % (size,100 * accu))

if __name__ == '__main__':
    x_train = np.loadtxt('final_train.txt', dtype=float)
    y_train = np.loadtxt('y_train.txt', dtype=float)
    x_validation = np.loadtxt('final_validation.txt', dtype=float)
    y_validation = np.loadtxt('y_validation.txt', dtype=float)
    x_test = np.loadtxt('final_test.txt', dtype=float)
    y_test = np.loadtxt('y_test.txt', dtype=float)

    predictor = train(x_train,y_train)
    validation(predictor,x_train,y_train)
    validation(predictor,x_validation,y_validation)
    validation(predictor,x_test,y_test)
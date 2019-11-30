import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(14, 60)
        self.fc2 = nn.Linear(60, 100)
        self.fc3 = nn.Linear(100, 48)
        self.fc4 = nn.Linear(48,10)
        self.fc5 = nn.Linear(10, 2)

    def forward(self, x):
        x = F.sigmoid(self.fc1(x))
        x = F.sigmoid(self.fc2(x))
        x = F.sigmoid(self.fc3(x))
        x = F.sigmoid(self.fc4(x))
        x = F.sigmoid(self.fc5(x))
        return x


net = Net()
print(net)

import torch.optim as optim
epoches = 1000
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(),lr = 0.01)

def accuracy(predicted,y):
    res = torch.tensor(predicted == y,dtype=torch.float)
    accu = torch.mean(res)
    size = len(predicted)
    print('Accuracy of the network on the %d test : %d %%' %(size,100 * accu))


def train(X,Y,epoches = 1000):
    total_loss = []
    for epoch in range(epoches):
        running_loss = 0
        optimizer.zero_grad()
        outputs = net(X)
        loss = criterion(outputs, Y)
        loss.backward()
        optimizer.step()
        running_loss += loss.item() * 1000
        # print(outputs.size())
        _, predicted = torch.max(outputs, 1)
        if (epoch % 20 == 1):
            accuracy(predicted, Y)
            print('[%d] loss: %.3f' %
                  (epoch + 1, running_loss))
            total_loss.append(running_loss)
            running_loss = 0.0
    total_loss = np.array(total_loss)
    #plt.plot(range(int(epoches/20)),total_loss,'r-')
    #plt.savefig('loss.jpg')
    #plt.show()


    print('Finished Training')

def validate(x_validation,y_validation):
    XValidation = torch.tensor(torch.from_numpy(x_validation),dtype=torch.float)
    YValidation = torch.tensor(torch.from_numpy(y_validation),dtype=torch.long)
    pre_Validation = net(XValidation)
    _,pre_Validation = torch.max(pre_Validation,1)
    print(pre_Validation.size())
    print(YValidation.size())
    accuracy(pre_Validation,YValidation)

if __name__ == '__main__':
    x_train = np.loadtxt('final_train.txt', dtype=float)
    y_train = np.loadtxt('y_train.txt', dtype=float)
    x_validation = np.loadtxt('final_validation.txt', dtype=float)
    y_validation = np.loadtxt('y_validation.txt', dtype=float)
    x_test = np.loadtxt('final_test.txt', dtype=float)
    y_test = np.loadtxt('y_test.txt', dtype=float)
    X = torch.tensor(x_train, dtype=torch.float32)
    Y = torch.tensor(y_train, dtype=torch.long)
    epoches = 1000
    train(X,Y,epoches)
    validate(x_validation,y_validation)
    validate(x_test,y_test)
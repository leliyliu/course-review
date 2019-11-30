import numpy as np
import re

def process_ques(Qinfo):
    for i in range(Qinfo.shape[0]):
        Qinfo[i,2] = Qinfo[i,2].count('SW')/20
        Qinfo[i,3] = Qinfo[i,3].count('W')/8
        Qinfo[i,4] = Qinfo[i,4].count('SW')/50
        Qinfo[i,5] = Qinfo[i,5].count('W')/12

    np.savetxt('Qinfo.txt',Qinfo,fmt='%s %s %s %s %s %s %s')
    return Qinfo

def process_user(user_info):
    user_info[:,18] = (user_info[:,18].astype(float) - 191)/100
    user_info[user_info == 'male'] = 0
    user_info[user_info == 'female'] = 1
    user_info[user_info == 'unknown'] = 4
    user_info[user_info == 'new'] = 3
    user_info[user_info == 'daily'] = 1
    user_info[user_info == 'weekly'] = 1
    user_info[user_info == 'monthly'] = 2
    user_info = np.delete(user_info, [2, 3, 4, 5, 6, 13, 14, 15, 16, 17], axis=1)

    np.savetxt('Uinfo.txt',user_info,fmt='%s %s %s %s %s %s %s %s %s %s %s')

    return user_info

def substract(a,b):
    a = np.array([int(s) for s in re.findall(r'\d+', a)])
    b = np.array([int(s) for s in re.findall(r'\d+', b)])
    res = 24*(a[0] - b[0]) + (a[1] - b[1])
    return res

def interest(source,dst1,dst2):
    res = 0
    if(source == '-1'):
        return 0
    for x in source:
        if(dst1 != '-1'):
            res += dst1.count(x)
        if(dst2 == '-1'):
            break
        for y in str(dst2).split(sep = ','):
            m = y.split(sep = ':')
            if(x == m[0]):
                res += float(m[1])
    return res/145

def concat(mqinfo,muinfo,train,filename):
    contain = []
    #for i in range(train.shape[0]):
    for i in range(train.shape[0]):
        if(i % 100 == 0):
            print(i)
        x = mqinfo[mqinfo[:,0]==train[i,0]]
        y = muinfo[muinfo[:,0]==train[i,1]]
        k1 = substract(train[i,2],x[0,1])
        k1 = 100 if (k1 == 0) else 1000/k1
        k2 = interest(x[0,6],y[0,9],y[0,10])
        k = np.array([k1, k2])
        z = np.concatenate((x[:,2:6],y[:,1:9],k.reshape(1,-1)),axis = 1)
        contain.append(z)
    contain = np.array(contain).reshape(-1,14)
    print(contain.shape)
    np.savetxt(filename,contain,fmt='%s %s %s %s %s %s %s %s %s %s %s %s %s %s')

def main():
    user_info = np.loadtxt('user_info.txt', dtype=str)
    ques_info = np.loadtxt('ques_info.txt', dtype=str)
    Uinfo = process_user(user_info)
    Qinfo = process_ques(ques_info)

    train = np.loadtxt('x_train.txt', dtype=str)
    validation = np.loadtxt('x_validation.txt', dtype=str)
    test = np.loadtxt('x_test.txt', dtype=str)

    Qinfo = np.loadtxt('Qinfo.txt',dtype=str)
    Uinfo = np.loadtxt('Uinfo.txt',dtype=str)
    concat(Qinfo, Uinfo, train, 'final_train.txt')
    concat(Qinfo, Uinfo, validation, 'final_validation.txt')
    concat(Qinfo, Uinfo, test, 'final_test.txt')

if __name__ == '__main__':
    main()



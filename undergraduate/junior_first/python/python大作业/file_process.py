import numpy as np

user_info = np.loadtxt('user_info.txt',dtype=str)
ques_info = np.loadtxt('ques_info.txt',dtype=str)

np.delete(user_info,[2,3,4,5,6],axis=1)

user_info[user_info == 'male'] = 1
user_info[user_info == 'female'] = -1
user_info[user_info == 'unknown'] = 0
user_info[user_info == 'new'] = -1
user_info[user_info == 'daily'] = 3
user_info[user_info == 'weekly'] = 2
user_info[user_info == 'monthly'] = 1

np.savetxt(user_info,'process_user.txt',fmt='%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s')
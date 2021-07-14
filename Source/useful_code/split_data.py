import os
import glob
import random
import pandas
import numpy as np

os.chdir("../../")


dir_label= ['label_1', 'label_2', 'label_3']
dir_cams = ['Binh_s cam', 'Ti_s cam', 'Kha_s cam']


path="Dataset/{}/Binh_s cam"
print(path)

X_train =[]
X_val = []
X_test=[]

y_train=[]
y_val=[]
y_test=[]
#print(k)

for label in dir_label:
    
    dir_img = [os.path.join(label,"{}",x) for x in os.listdir(path.format(label)) if "Still" in x]

    random.shuffle(dir_img)
   
    categ   = [label] * len(dir_img)

    n = len(dir_img)

    X_test += dir_img[: int(0.1*n)] 
    y_test += [label] * len(dir_img[: int(0.1*n)])

    X_val += dir_img[ int(0.1*n): int(0.22*int(0.9*n))+int(0.1*n)]
    y_val += [label] * len(dir_img[ int(0.1*n): int(0.22*int(0.9*n))+int(0.1*n)])

    X_train += dir_img[int(0.22*int(0.9*n))+int(0.1*n):] 
    y_train += [label] * len(dir_img[int(0.22*int(0.9*n))+int(0.1*n):])


print(len(X_train))
print(len(X_val))
print(len(X_test))

print()

print(len(y_train))
print(len(y_val))
print(len(y_test))


if os.path.exists("Dataset/csv") is False:
    os.mkdir("Dataset/csv")


#____________________________ train
temp =list(zip(X_train,y_train))
random.shuffle(temp)

a,b= zip(*temp)

d= {"path":a, "label":b}

train= pandas.DataFrame(data=d)
train.to_csv("Dataset/csv/train.csv")

#______________________________val
temp =list(zip(X_val,y_val))
random.shuffle(temp)

a,b= zip(*temp)

d= {"path":a, "label":b}

train= pandas.DataFrame(data=d)
train.to_csv("Dataset/csv/val.csv")

#____________________________test
temp =list(zip(X_test,y_test))
random.shuffle(temp)

a,b= zip(*temp)

d= {"path":a, "label":b}

train= pandas.DataFrame(data=d)
train.to_csv("Dataset/csv/test.csv")





#le = LabelEncoder()
#labels = le.fit_transform(y_label)
# One-hot encoding/



#return dir_cams,np.array(X_dir), np.array(y_label)
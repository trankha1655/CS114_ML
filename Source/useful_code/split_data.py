import os

import random
import pandas
import numpy as np


def split_img():
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
        
        dir_img = [ label+"/{}/"+x for x in os.listdir(path.format(label)) if "Still" in x]

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

def split_oneside():
    os.chdir("../../")
    
    path= "Dataset/one_side/{}/{}/{}"

    tps = ["train","test"]
    dir_label= ['label_1', 'label_2', 'label_3']

    
    
    def get_test():
        temp=[]
        y_ = []
        for label in dir_label:
            dir_img = [ "{}/test"+label + x for x in os.listdir(path.format("crop_mask","test",label)) \
                                if "Still" in x]
            
            temp+= dir_img
            y_  += [label]*len(dir_img)

        
        zp =list(zip(temp,y_))
        random.shuffle(zp)

        a,b= zip(*zp)

        d= {"path":a, "label":b}

        test= pandas.DataFrame(data=d)
        #train.to_csv("Dataset/csv/test.csv")

        return test

    def get_train_val():

        train=[]
        ytr = []
        val= []
        yvl=[]
        for label in dir_label:
            dir_img = [ "{}/train/"+label+"/" + x                                           \
            
                                for x in os.listdir(path.format("crop_mask","train",label)) \
                                
                                if "Still" in x]

            n = len(dir_img)
            y_ = [label]*n
            random.shuffle(dir_img)

            val += dir_img[: int(0.15*n)]
            train   += dir_img[int(0.15*n): ]

            yvl   += y_[: int(0.15*n)]
            ytr   += y_[int(0.15*n): ]
            

        #train.to_csv("Dataset/csv/test.csv")
        zp =list(zip(train,ytr))
        random.shuffle(zp)

        a,b= zip(*zp)

        d= {"path":a, "label":b}

        df_train= pandas.DataFrame(data=d)
        

        #val to csv()
        zp =list(zip(val,yvl))
        random.shuffle(zp)

        a,b= zip(*zp)

        d= {"path":a, "label":b}

        df_val= pandas.DataFrame(data=d)

        return df_train , df_val

    df_test= get_test()

    df_train, df_val = get_train_val()

    df_test.to_csv("Dataset/one_side/test.csv")
    df_train.to_csv("Dataset/one_side/train.csv")
    df_val.to_csv("Dataset/one_side/val.csv")

    



    

#le = LabelEncoder()
#labels = le.fit_transform(y_label)
# One-hot encoding/
split_oneside()


#return dir_cams,np.array(X_dir), np.array(y_label)
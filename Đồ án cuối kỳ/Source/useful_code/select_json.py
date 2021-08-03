
import os
import random
import pandas 
os.chdir("../../")

def check_sync():
    paths="Dataset/json/{}/"

    dir_label= ['label_1', 'label_2',"label_3"]
    dir_cams = ['Binh_s cam', 'Ti_s cam', 'Kha_s cam']

    for cam in dir_cams:

        for label in dir_label:
            path= paths.format(label)
            img_paths= [ path+"{}/"+ x for x in os.listdir(path+cam) ]
                            


            for x in img_paths:
                for cam1 in dir_cams:
                    if not os.path.exists(x.format(cam1)):
                        print(x.format(cam1))

            print("end.")




def find():
    
    jdir= "Dataset/json/{}/{}" #{} is name Label
    dir_label= ['label_1', 'label_2']
    dir_cams = ['Binh_s cam', 'Ti_s cam', 'Kha_s cam']

    imdir= "Dataset/img/"

    js= []
    ims=[]
    for label in dir_label:
        head= "json/"+label
        
        temp=[]
        _,j=   zip(*[    ( l+"/{}/".format(cam) + x[:-4]+"jpg",    label +"/{}/".format(cam) + x )                                               \
                      for cam in dir_cams for l in dir_label  for x in os.listdir(jdir.format(label,dir_cams[0])) \

                                if os.path.exists( imdir+l + "/{}/".format(dir_cams[0]) + x[:-4]+"jpg")  ] ) 

    
        ims+= list(_)
        js+= list(j)
        

    c = list(zip(ims,js))
    random.shuffle(c)
    a, b = zip(*c)

    im_val= a[:200]
    j_val = b[:200]

    im_train = a[200:]
    j_train = b[200:]

    d= {"path":im_train, "label":j_train}

    train= pandas.DataFrame(data=d)
    train.to_csv("Dataset/csv/train_mask.csv")

    d= {"path":im_val, "label":j_val}

    train= pandas.DataFrame(data=d)
    train.to_csv("Dataset/csv/val_mask.csv")

        
        
            
            

    

#check_sync()

find()
            


            

        






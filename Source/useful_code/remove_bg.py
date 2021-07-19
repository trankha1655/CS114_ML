import segmentation_models
from segmentation_models import Unet
from segmentation_models import get_preprocessing
from segmentation_models.losses import bce_jaccard_loss
from segmentation_models.metrics import iou_score
from tensorflow.keras.applications.vgg16 import VGG16 , preprocess_input as pp_vgg16,decode_predictions as dpvgg
import os
from tensorflow.keras.preprocessing.image import img_to_array, array_to_img, load_img
import get_data
import numpy as np
import cv2
import time
import tensorflow as tf

#/setup model_______________________
os.chdir("../../../")

segmentation_models.set_framework('tf.keras')
model = Unet( encoder_weights='imagenet')
model.compile('Adam', loss=bce_jaccard_loss, metrics=[iou_score])

model.load_weights("CS114_ML/Source/Model/unet_bg_vgg.h5")



#tf.debugging.set_log_device_placement(True)

#-----------------------------------------\

#/ read path and create storing folder_____

def crop_img_3side(model):

    INPUT_SHAPE= (320,640,3)
    clone = np.zeros((1,INPUT_SHAPE[0],INPUT_SHAPE[1],INPUT_SHAPE[2]))

    path="CS114_ML\Dataset\{}"


            #find label
    list_label= [x for x in os.listdir(path.format("")) if "label" in x]

            #get path by function 
    cams, X,y = get_data.getPaths(path.format("img"))


    temp = "CS114_ML\Dataset\crop_mask"
        


    #creat folder Dataset/crop_mask   if doesnt exist
    if os.path.exists(temp) is False:
        os.mkdir(temp)

    #creat 3 folder : label1-3
    for label in list_label:
        if not os.path.exists(os.path.join(temp,label)):
            os.mkdir(os.path.join(temp,label))
            
    #creat 3 cam in each other label
    for label in list_label:
        for cam in cams:
            if not os.path.exists(os.path.join(temp,label,cam)):
                os.mkdir(os.path.join(temp,label,cam))








    now= time.time()
    for i in range(len(X)):

        

        for cam in cams:
            st= time.time()
            
            

            dirc= os.path.join(path,y[i],cam,X[i])
            
            if os.path.exists(dirc.format("crop_mask")[:-3]+"png"):
                continue

            #read image
            img = load_img(dirc.format("img"), target_size=(320,640)) 
            img = img_to_array(img)
            clone[0] = img
            im = clone.copy().astype("int32")[0]

            #predict mask
            y_pre=None
            try:
        # Specify an invalid GPU device
                with tf.device('/device:GPU:2'):
                    y_pre= model.predict(pp_vgg16(clone))[0]
            except RuntimeError as e:
                print(e)
            
            
            
            

            #crop follow mask
            binary_predicted_mask = np.where(y_pre[:,:,0] > 0.5, 1, 0)
            binary_predicted_mask= binary_predicted_mask.astype(np.int8)

            fg = cv2.bitwise_or(im, im, mask=binary_predicted_mask)
            fg  = array_to_img(fg)
            fg.save(dirc.format("crop_mask")[:-3]+"png")

            ed= time.time()
            print("{}{}. time to process: {}".format(i,cam,ed-st))

    then= time.time()

    print("2028 img was processed in {}".format(then-then))


def crop_img_1side(model):

    tps= ["test","train"]
    path="CS114_ML\Dataset\one_side\{}\{}"


            #find label
    list_label= [x for x in os.listdir(path.format("",tps[0])) if "label" in x]

            #get path by function 
    '''
    cams, X,y = get_data.getPaths(path.format(""))
    '''
    temp = "CS114_ML\Dataset\one_side\crop_mask"
    
    INPUT_SHAPE= (320,640,3)
    clone = np.zeros((1,INPUT_SHAPE[0],INPUT_SHAPE[1],INPUT_SHAPE[2]))

    #creat folder Dataset/one_side/crop_mask   if doesnt exist
    if os.path.exists(temp) is False:
        os.mkdir(temp)

    

    #creat 2 folder train and test
    for tp in tps:
        if not os.path.exists(os.path.join(temp,tp)):
            os.mkdir(os.path.join(temp,tp))
            
    #creat 3 label in each other [train, test]
    for tp in tps:
        for label in list_label:
            if not os.path.exists(os.path.join(temp,tp,label)):
                os.mkdir(os.path.join(temp,tp,label))



    count=0
    then= time.time()
    for tp in tps:

        cams, X,y = get_data.getPaths(path.format("",tp),one_view=True )
        count+= len(X)

        for i in range(len(X)):
            st= time.time()
            
            dirc= os.path.join(path,y[i],X[i])
            
            if os.path.exists(dirc.format("crop_mask",tp)[:-3]+"png"):
                continue

            #read image
            img = load_img(dirc.format("",tp), target_size=(320,640)) 
            img = img_to_array(img)
            clone[0] = img
            im = clone.copy().astype("int32")[0]

            #predict mask
            #y_pre=None
            #try:
        # Specify an invalid GPU device
                #with tf.device('/device:GPU:2'):
            y_pre= model.predict(pp_vgg16(clone))[0]
            #except RuntimeError as e:
             #   print(e)
            
            
            
            

            #crop follow mask
            binary_predicted_mask = np.where(y_pre[:,:,0] > 0.5, 1, 0)
            binary_predicted_mask= binary_predicted_mask.astype(np.int8)

            fg = cv2.bitwise_or(im, im, mask=binary_predicted_mask)
            fg  = array_to_img(fg)
            fg.save(dirc.format("crop_mask",tp)[:-3]+"png")
            

            ed= time.time()
            print("{}{}. time to process: {}".format(tp,i,ed-st))




    then= time.time()

    print("{} img was processed in {}".format(count,then-then))


crop_img_1side(model)

    
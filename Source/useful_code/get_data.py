from tensorflow.keras.utils import Sequence
import os
from tensorflow.keras.applications.vgg16 import VGG16 , preprocess_input as pp_vgg16,decode_predictions as dpvgg
from segmentation_models import Unet
from segmentation_models import get_preprocessing
from segmentation_models.losses import bce_jaccard_loss
from segmentation_models.metrics import iou_score
import numpy as np
from sklearn.preprocessing import LabelEncoder,LabelBinarizer

from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img

import albumentations as A
import cv2


def getPaths(path): 
    
    dir_label= os.listdir(path)
    

    ex2=[]
    for x in dir_label:
      if 'label' in x:
        ex2.append(x)

    dir_label= ex2

    dir_cams = ['Binh_s cam', 'Kha_s cam', 'Ti_s cam']

    

    cam= dir_cams[0]
    X_dir=[]
    y_label=[]
    for label in dir_label:
        if '.' not in label:
            dir_img = os.listdir(os.path.join(path,label,cam))
            final=[]
            for x in dir_img:
                if "Still" in x:
                    final.append(x)
            categ   = [label] * len(final)
            X_dir+= final
            y_label+=(categ)

    #le = LabelEncoder()
    #labels = le.fit_transform(y_label)
    # One-hot encoding/
    


    return dir_cams,np.array(X_dir), np.array(y_label)

class ProteinDataGenerator(Sequence):
            
    def __init__(self,
                paths, 
                labels,  
                shape,
                dir ,
                batch_size=32,
                mask=False, 
                shuffle = False, 
                cams='',
                preprocess_input=None):

        self.paths, self.labels = paths, labels
        self.batch_size = batch_size
        self.shape = shape
        self.shuffle = shuffle
        self.use_cache = use_cache
        self.cams= cams
        self.dir= dir #"/content/Dataset/{}"  {} is json or not
        self.preprocess_input = preprocess_input
        self.mask= mask
        if self.mask:

            self.backbone= "vgg16"
            self.mpp= get_preprocessing(self.backbone)
            self.model = Unet(self.backbone, encoder_weights='imagenet')
            self.model.load_weights("/content/drive/MyDrive/model_h5/unet_bg_vgg.h5")
            
                
            self.pre_clone= np.zeros((1,320,640,3))

        if self.mask:
            temp=[]
            for i in range(len(paths)):
              for cam in cams:
                temp.append(os.path.join(labels[i],cam,paths[i]))
                #example: label_1/Kha's cam/Binh_cam.00_03_50_20.Still004.jpg

            self.paths= np.asarray(temp)
  

        self.on_epoch_end()      

    
    def __len__(self):
        return int(np.ceil(len(self.paths) / float(self.batch_size)))
    
    def __getitem__(self, idx):

        if not self.mask:

            #list index for generate
            indexes = self.indexes[idx * self.batch_size : (idx+1) * self.batch_size]

            #list path with its indexs
            paths = self.paths[indexes]
            # create X for generate
            X = np.zeros((paths.shape[0],3, self.shape[0], self.shape[1], self.shape[2]))
            #print(X.shape)
            #clone_img= np.zeros_like(shape)

            y = self.labels[indexes]
            #print(y.shape)
            # Generate data
            
            for i, path in enumerate(paths):
                image = self.__load_image(path,self.labels[indexes[i]])
                X[i][0], X[i][1], X[i][2] = image[0], image[1], image[2]
            X[:,0,] = self.preprocess_input( X[:,0,])
            X[:,1,] = self.preprocess_input(X[:,1,])
            X[:,2,] = self.preprocess_input(X[:,2,])

            
            le = LabelEncoder()
            labels = le.fit_transform(y)
            # One-hot encoding
            lb = LabelBinarizer()
            labels = lb.fit_transform(labels)
            #print(labels.shape)
            
            return X, labels

        else: #USING MASK FOR SEGMENTATION 
            #list index for generate
            indexes = self.indexes[idx * self.batch_size : (idx+1) * self.batch_size]

            #list path with its indexs
            paths = self.paths[indexes]
            # create X for generate
            X = np.zeros((paths.shape[0], self.shape[0], self.shape[1], self.shape[2]))

            y_mask = np.zeros((paths.shape[0], self.shape[0], self.shape[1]))
            #print(X.shape)
            #clone_img= np.zeros_like(shape)

            #y = self.labels[indexes]
            #print(y.shape)
            # Generate data
            
            for i, path in enumerate(paths):
                image = self.__load_image(path)
                mask  = self.__load_mask(path)
                
                X[i]= image
                y_mask[i]= mask


            X= preprocess_input(X)
            
            return X, y_mask
    


    def on_epoch_end(self):
        
        # Updates indexes after each epoch
        self.indexes = np.arange(len(self.paths))
        if self.shuffle == True:
            np.random.shuffle(self.indexes)

    def __iter__(self):
        """Create a generator that iterate over the Sequence."""
        for item in (self[i] for i in range(len(self))):
            yield item
            
    def __load_image(self, path,label=None):
        

        if self.mask:
            full_path= os.path.join(self.dir,path) # full_path = "/content/Dataset/{}/label_1/Kha's cam/Binh_cam.00_03_50_20.Still004.jpg"
            img = load_img(full_path.format(""), target_size=self.shape[:2]) 
            img = img_to_array(img)
            

            return img

        else:




            full_path= os.path.join(self.dir,label,"{}",path)
            
            x= []
            for cam in self.cams: 
                
                img = self.img_crop_mask(full_path.format("",cam))
                # Add one more dimension
                img = np.expand_dims(img, axis=0)
                # preprocess the images using preprocess_input() from inception module
                #img=self.preprocess_input(img)

                x.append(img)

            return x
    
    def img_crop_mask(self,path):
        #load img
        img = load_img(path, target_size=(320,640))
        img = img_to_array(img)
        self.pre_clone[0] = img
        
        #predict_mask
        predicted_mask= self.model.predict(pp_vgg16(self.pre_clone.copy()))
        binary_predicted_mask = np.where(predicted_mask[0] > 0.5, 1, 0)
        fg= binary_predicted_mask.copy().astype(np.int8)
        # crop follow mask
        img= cv2.bitwise_or(img, img, mask=fg)

        #resize
        loader = A.Compose([
            A.Resize(width=299, height=299),
        ])

        clone= loader(image=img)["image"]

        
        return clone

    def json2mask(self,path):

        data = json.load(open(path))
        

        #mask = Image.open(mask_path).convert('L') # Use mask.mode to know that the format of the read mask image is I, which is 32-bit integer data, so it must be converted to L format
        # Change to read directly from json file
        label_name_to_value = {"_background_": 0,"1":1,"2":2}
        mask, label_names = shape.shapes_to_label(img_shape=(720,1280), shapes=data['shapes'],label_name_to_value=label_name_to_value)
        
        obj_ids = np.unique(mask)  # Remove duplicate numbers in the array and sort
        obj_ids = obj_ids[1:]  # Remove the first index because it is the background
        masks = mask == obj_ids[:, None, None]  # split the color-encoded mask into a set of binary masks

        mask= mask.astype("float32")

        loader = A.Compose([
            A.Resize(width=self.shape[1], height=self.shape[0]),
        ])

        

        clone= loader(image=mask)["image"]
        clone= 255*clone

        ret, thresh1 = cv2.threshold(clone, 120, 255, cv2.THRESH_BINARY)
        thresh1= thresh1/255
        thresh1= thresh1.astype("int32")
        
        return thresh1

        

    def __load_mask(self, path,label=None):

        path= path[:-3] +"{}"
        full_path= os.path.join(self.dir,path)
        img = self.json2mask(full_path.format("json","json"))

        return img
        

        


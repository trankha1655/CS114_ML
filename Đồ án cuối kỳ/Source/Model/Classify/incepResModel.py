
from tensorflow.keras.layers import  Maximum,Reshape,Concatenate,Input,Dropout,Conv2D , Flatten , \
                Dense , MaxPool2D , BatchNormalization , GlobalAveragePooling2D

from tensorflow.keras.applications.inception_resnet_v2 import InceptionResNetV2 
from tensorflow.keras.models import Model
def get_model():

    def base_model():

        base_model = InceptionResNetV2(include_top= False , weights='imagenet')

        for x in base_model.layers:
            x.trainable =True


        z = base_model.output
        z = GlobalAveragePooling2D()(z)
        z = BatchNormalization()(z)
        

        model= Model(inputs=base_model.input,outputs=z)
        #model.load_weights("/content/drive/MyDrive/model_h5/1side_incepres_ep2_2_0.82.h5")
        
        

        return model


    def FC_model():
        inputs = Input(shape=(3,299,299,3))
        model = base_model()
        model1 = base_model()
        model2 = base_model()
        
        
        y1 = model(inputs[:,0,])
        y2 = model1(inputs[:,1,])
        y3 = model2(inputs[:,2,])

        combined = Maximum()([y1, y2, y3])
        output = Dropout(0.5)(combined)
        output = Dense(1024, activation="relu")(output)
        output = BatchNormalization()(output)
        output = Dropout(0.5)(output)
        output = Dense(3, activation='softmax')(output)
        ensemble_model = Model(inputs=inputs, outputs=output)

        return ensemble_model

    final = FC_model()
    for layer in final.layers:
        layer.trainable=False
    return final




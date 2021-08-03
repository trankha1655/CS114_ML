
import tensorflow as tf
from tensorflow.keras.models import load_model
import os

os.chdir("../../")



def unet():
    path="Source\Model\Model_Unet_0.95.h5"
    model= load_model(path)
    return model

def incepRes():
    path="Source\Model\Model_inception_0.81.h5"
    model= load_model(path)
    return model


def MbNetv2():
    path="Source\Model\Model_DraFru_MbNet_0.77.h5"
    model load_model(path)
    return model




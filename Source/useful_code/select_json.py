
import os

os.chdir("../../")
paths="Dataset/crop_mask/{}/"

dir_label= ['label_1', 'label_2', 'label_3']
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


import os
os.chdir("../../../")

path="Dataset/img/label_2/"

dir_label= ['label_1', 'label_2', 'label_3']
dir_cams = ['Binh_s cam', 'Ti_s cam', 'Kha_s cam']

#img_paths= [ path+"{}/"+ x for x in os.listdir(path+dir_cams[0]+"/") ]
                
os.listdir("Dataset/img/label_2/Binh_s cam/")

for x in img:
    for cam in dir_cams:
        if not os.path.exists(x.format(cam)):
            print(x)

print("end.")

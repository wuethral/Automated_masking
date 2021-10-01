import os
import matplotlib as plt
#directory = 'C:/Users/wuethral/Desktop/Automated_Masking/pilers(video34)/original_images'
directory = 'D:/hololens_recordings/Project_Balgrist/hands/video_29.9.21/PV - Copy'
image_nr = 1
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        source_path = directory + '/' + filename
        #destination_path = 'C:/Users/wuethral/Desktop/Automated_Masking/pilers(video34)/original_images_renamed/image_' + str(image_nr) + '.png'
        destination_path =  'D:/masks/hands/original_images_renamed/hands_image_' + str(image_nr) + '.png'
        os.rename(source_path, destination_path)
        image_nr += 1


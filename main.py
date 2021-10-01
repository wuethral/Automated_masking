from myComputerVisonLib import MergingMasks, canny_edge_det, hsv_filter, DbScan, morphological_operation, fill_hole, SwitchingBlackWhite

import cv2 as cv
import numpy as np
from PIL import Image
import os
directory =  'D:/masks/pliers(video34)_3/original_images_renamed'
img_nr = 1
for bla in os.listdir(directory):

    filename = 'image_' + str(img_nr) + '.png'
    print(filename)
    path_original_image = directory + '/' + filename
    img = cv.imread(path_original_image)
    hsv_filter(img_nr, img)
    canny_edge_det(img_nr, img)
    path_canny = 'D:/masks/pliers(video34)_3/canny_edge_images/canny_edge_mask_'+ str(img_nr) +'.png'
    path_hsv = 'D:/masks/pliers(video34)_3/hsv_filter_images/hsv_mask_'+ str(img_nr) +'.png'
    mask_canny_edge_detection = Image.open(path_canny)
    mask_hsv_filter = Image.open(path_hsv)
    height = mask_hsv_filter.height
    width = mask_hsv_filter.width
    ''' 

    MergingMasks(img_nr, mask_canny_edge_detection, mask_hsv_filter, height, width)
    source_path = "D:/masks/hands/final_mask_no_morph/final_mask_no_morph_" + str(
        img_nr) + '.png'
    destination_path = "D:/masks/hands/final_mask_with_morph/final_mask_with_morph_" + str(
        img_nr) + '.png'
    morphological_operation(img_nr, source_path, destination_path)
    DbScan(img_nr, destination_path, input_img_with_canny = True)
    path_in = "D:/masks/hands/hsv_canny_dbscan/mask_hsv_canny_dbscan_" + str(
        img_nr) + '.png'
    mask_in = cv.imread(path_in, 0)
    path_out = "D:/masks/hands/hsv_canny_dbscan_holes_filled/mask_hsv_canny_dbscan_holes_filled_" + str(
        img_nr) + '.png'
    mask_out = fill_hole(mask_in)
    cv.imwrite(path_out, mask_out)
    '''

    SwitchingBlackWhite(img_nr, mask_hsv_filter, height, width)
    path = "D:/masks/pliers(video34)_3/hsv_switch_bw/hsv_switch_bw_" + str(img_nr) + '.png'
    DbScan(img_nr, path, input_img_with_canny=False)
    source_path = "D:/masks/pliers(video34)_3/hsv_dbscan(no_canny)/mask_hsv_dbscan_" + str(
        img_nr) + '.png'
    destination_path = "D:/pliers(video34)_3/hsv_dbscan_morph(no_canny)/mask_hsv_dbscan_morph_" + str(
        img_nr) + '.png'
    morphological_operation(img_nr, source_path, destination_path)
    path_in = "D:/masks/pliers(video34)_3/hsv_dbscan_morph(no_canny)/mask_hsv_dbscan_morph_" + str(
        img_nr) + '.png'
    mask_in = cv.imread(path_in, 0)
    path_out = "D:/masks/pliers(video34)_3/hsv_dbscan_morph_holes_filled(no_canny)/pliers_video34_mask_hsv_dbscan_morph_holels_filled" + str(
        img_nr) + '.png'
    mask_out = fill_hole(mask_in)
    
    cv.imwrite(path_out, mask_out)
    '''
    SwitchingBlackWhite(img_nr, mask_hsv_filter, height, width)
    '''

    img_nr += 1

    

    


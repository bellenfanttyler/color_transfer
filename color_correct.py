# -*- coding: utf-8 -*-
# import the necessary packages
from color_transfer import color_transfer
import numpy as np
import argparse
import cv2
import os
import glob


save_directory = os.getcwd() + "/corrected_images/"
os.makedirs(save_directory, exist_ok=True)


source_directory = "/Users/tylerbellenfant/Documents/Satellite_Images/UCMerced_LandUse/Images/forest/*.tif"
target_directory = "/Users/tylerbellenfant/Documents/Satellite_Images/UCMerced_LandUse/Images/forest/*.tif"

source_files = sorted(glob.glob(source_directory))
target_files = sorted(glob.glob(target_directory), reverse = True)

for i in range(len(source_files)):
    
    try:
        source = cv2.imread(source_files[i])
        target = cv2.imread(target_files[i])
        
        # transfer the color distribution from the source image
        # to the target image
        transfer = color_transfer(source, target, clip = True , preserve_paper= True)
        transfer_name = save_directory + os.path.basename(target_files[i])
        
        cv2.imwrite(transfer_name, transfer)
        
    except Exception as e: print(e)


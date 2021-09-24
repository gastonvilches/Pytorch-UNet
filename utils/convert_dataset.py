import os
from PIL import Image
import numpy as np

def convert_dataset(input_dir, output_dir, is_mask):
    if is_mask:
        # Masks processing
        folders_list = os.listdir(input_dir)
        num_folders = len(folders_list)
        for idx, folder in enumerate(folders_list):
            print('Mask folder', idx, '/', num_folders)
            for file in os.listdir(input_dir + '/' + folder):
                input_path = input_dir + '/' + folder + '/' + file
                output_path = output_dir + '/' + folder + '_' + file
                img = np.array(Image.open(input_path).convert(mode='L'))
                img2 = Image.fromarray(255-img)
                img2.save(output_path)
    else:
        # Images processing
        folders_list = os.listdir(input_dir)
        num_folders = len(folders_list)
        for idx, folder in enumerate(folders_list):
            print('Img folder', idx, '/', num_folders)
            for file in os.listdir(input_dir + '/' + folder):
                input_path = input_dir + '/' + folder + '/' + file
                output_path = output_dir + '/' + folder + '_' + file
                img = np.array(Image.open(input_path).convert(mode='L'))
                img2 = np.zeros(img.shape, dtype=np.uint8)
                img2[img < 255] = 255
                img3 = Image.fromarray(img2)
                img3.save(output_path)
        



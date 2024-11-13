import cv2
import numpy as np
import os
from concurrent.futures import ProcessPoolExecutor
from glob import glob


input_dir = 'input'   # folder with your input files
output_dir = 'output'    # folder to save the mask images outputs



# counter for the total pixel count
total_pixel_count = 0

def process_image(file_path):
    
    image = cv2.imread(file_path)
    if image is None:
        return 0  
    
    # creates mask where all channels are above 200
    mask = cv2.inRange(image, (200, 200, 200), (255, 255, 255))
    
    # count of non-zero pixels
    pixel_count = cv2.countNonZero(mask)
    
    # writing masks as png 
    mask_filename = os.path.join(output_dir, os.path.basename(file_path).replace('.jpg', '_mask.png'))
    cv2.imwrite(mask_filename, mask)
    
    return pixel_count

def main():
    global total_pixel_count
    
    
    image_files = glob(os.path.join(input_dir, '*.jpg'))
    
    # parallel processing
    with ProcessPoolExecutor() as executor:
        pixel_counts = executor.map(process_image, image_files)
    
    # sum up the pixel counts from each image
    total_pixel_count = sum(pixel_counts)
    
    # print the total pixel count
    print(f"Total pixels where the mask is max in all images: {total_pixel_count}")

if __name__ == "__main__":
    main()

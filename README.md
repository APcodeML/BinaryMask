# Image Mask Generator

This script reads JPG files from a directory, creates binary masks based on pixel intensity, and saves the masks as PNG files. It also logs the total count of pixels where the mask is max (all three channels are above 200).

## Requirements
- OpenCV
- NumPy
  
## Installation
Install the required packages with:

- pip install -r requirements.txt


## Usage

- Place your JPG files in the input folder.

- Run the script:

  python mask.py

- The binary masks will be saved in the output folder, and the total pixel count will be logged to the console.

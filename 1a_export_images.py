import os
from PIL import Image,ImageOps

# Define the source and destination directories
source_dir = 'C:/tool/gaussian-splatting/source_data/guitar/original'
dest_dir = 'C:/tool/gaussian-splatting/source_data/guitar/images'

# Create the destination directory if it doesn't exist
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Loop through all files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.JPG')):  # Add any other image formats if needed
        # Open the image file
        img_path = os.path.join(source_dir, filename)
        with Image.open(img_path) as img:
            # Adjust orientation based on EXIF data
            img = ImageOps.exif_transpose(img)
            # Resave the image to the destination directory
            dest_path = os.path.join(dest_dir, filename)
            img.save(dest_path)

print("Images have been successfully copied and resaved.")

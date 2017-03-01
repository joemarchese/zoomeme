# Program designed to take in input image and provide three zoomed in images
# (Eventually, and hopefully on the face)

import os, sys
import urllib.request
from PIL import Image

# Generate Path Names
if not os.path.exists(os.getcwd() + '\\Memes'):
    os.mkdir(os.getcwd() + '\\Memes')
os.chdir(os.getcwd() + '\\Memes')
outfile = 'zoom.jpg'
outfile_two = 'zoom_two.jpg'
outfile_three = 'zoom_three.jpg'
four_outfile = 'meme.jpg'

# Get Input File From The Innanets
infile = input('Please Enter Full URL for the Image: ')
infile = urllib.request.urlretrieve(infile, infile.split('/')[-1])

# Process the Input Image
image = Image.open(infile[0])
width, height = image.size
crop_size = (round(.10 * width), round(.10 * height), round(.90 * width), round(.90 * height))
zoom = image.crop(crop_size)
zoom = zoom.resize(image.size, resample=Image.BICUBIC)
zoom_two = zoom.crop(crop_size)
zoom_two = zoom_two.resize(image.size, resample=Image.BICUBIC)
zoom_three = zoom_two.crop(crop_size)
zoom_three = zoom_three.resize(image.size, resample=Image.BICUBIC)

# Build the Meme
four_image = Image.new('RGBA', ((width * 2), (height * 2)), 'white')
four_image.paste(image, (0, 0))
four_image.paste(zoom, (width, 0))
four_image.paste(zoom_two, (0, height))
four_image.paste(zoom_three, (width, height))

# Save the Memes
zoom.save(outfile, 'JPEG')
zoom_two.save(outfile_two, 'JPEG')
zoom_three.save(outfile_three, 'JPEG')
four_image.save(four_outfile, 'JPEG')

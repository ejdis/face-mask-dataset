import os
from PIL import Image

# Set directory path
from_directory = 'old_png/'
to_directory = 'img/'

# Set from and to extension
from_ = '.png'
to_ = '.jpg'

#
#   Converte tutte le immagini contenute in 'from_directory' con estensione 'from_' 
#   in immagini con estensione 'to_' e le salva nella directory 'to_directory'
#

if not os.path.exists(to_directory):
    os.makedirs(to_directory)


for filename in os.listdir(from_directory):
    if filename.endswith(from_):
        # Open the image file
        img = Image.open(from_directory + filename)

        print(f'Converto {filename}...')

        # Convert the image to RGB format
        rgb_img = img.convert('RGB')

        # Save the image 
        new_filename = filename.replace(from_, to_)
        rgb_img.save(to_directory + new_filename)


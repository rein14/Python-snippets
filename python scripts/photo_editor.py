from PIL import Image, ImageEnhance, ImageFilter

import os

parent_dir = os.curdir
print(parent_dir)
path = os.path.join(parent_dir, 'editedimgs')
if not path:
    os.mkdir(path)

photo_paths ='./imgs'
pathout = "./editedimgs"

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}",)
    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]
    edit.save(f'.{pathout}/{clean_name}_edited.jpg')
from django.conf import settings
from django.core.files import File
import os
import shutil
from PIL import Image
import random


def create_new_thumb(media_path, instance, owner_slug, max_width, max_height):
    filename = os.path.basename(media_path)
    print("filename : %s" % filename)
    thumb = Image.open(media_path)
    width, height = thumb.size
    # size = (max_height, max_width)
    # aspect_ratio = width / height

    if width < max_width and height < max_height:  # her ikisi de kısa ise
        # hangi tarafa doğru genişletmek gerek bul
        if width / max_width < height / max_height:  # enden genişleyecek, boydan kırpılacak
            # print("her ikisi de kısa, enden genişleyecek, boydan kırpılacak")
            thumb = enden_genislet_boydan_kirp(width, height, max_width, max_height, thumb)
        else:  # boydan genişleyecek, enden kırpılacak
            # print("her ikisi de kısa, boydan genişleyecek, enden kırpılacak")
            thumb = boydan_genislet_enden_kirp(width, height, max_width, max_height, thumb)
    elif width < max_width and height >= max_height:  # en küçük boy değil
        # print("en kısa boy değil, enden genişleyecek, boydan kırpılacak")
        thumb = enden_genislet_boydan_kirp(width, height, max_width, max_height, thumb)
    elif width >= max_width and height < max_height:  # boy küçük en değil
        # print("boy kısa en değil, boydan genişleyecek, enden kırpılacak")
        thumb = boydan_genislet_enden_kirp(width, height, max_width, max_height, thumb)
    elif width >= max_width and height >= max_height:  # her ikisi de büyük o yüzden resize yok.
        # print("her ikisi de büyük o yüzden resize yok. Bu hatalı resize olacak yine")
        if width / max_width > height / max_height:  # enden kırpılacak
            # print("enden kırparak thumb yarat.")
            thumb = enden_kirparak_thumb_yarat(width, height, max_width, max_height, thumb)
        elif width / max_width < height / max_height:
            # print("boydan kırparak thumb yarat.")
            thumb = boydan_kirparak_thumb_yarat(width, height, max_width, max_height, thumb)
        else:
            new_size = (max_width, max_height)
            thumb.thumbnail(new_size, Image.ANTIALIAS)
            # print(thumb)

    temp_loc = "%s/%s/tmp" % (settings.MEDIA_ROOT + "/products", owner_slug)
    print("temp_loc : %s" % temp_loc)
    if not os.path.exists(temp_loc):
        os.makedirs(temp_loc)
    temp_file_path = os.path.join(temp_loc, filename)
    if os.path.exists(temp_file_path):
        temp_path = os.path.join(temp_loc, "%s" % (random.random()))
        os.makedirs(temp_path)
        temp_file_path = os.path.join(temp_path, filename)

    temp_image = open(temp_file_path, "wb")

    print("temp_image : %s" % temp_image)
    thumb.save(temp_image, "JPEG")
    print("thumb : %s" % thumb)
    thumb_data = open(temp_file_path, "rb")
    thumb_file = File(thumb_data)
    print("thumb_file : %s" % thumb_file)
    instance.media.save(filename, thumb_file)
    shutil.rmtree(temp_loc, ignore_errors=True)
    return True


def boydan_kirparak_thumb_yarat(width, height, max_width, max_height, thumb):
    resize_ratio = max_width / width
    new_size = (height * resize_ratio, height * resize_ratio)
    thumb.thumbnail(new_size, Image.ANTIALIAS)
    new_width, new_heigth = thumb.size
    crop_size = (new_heigth - max_height) // 2
    # thumb.crop(left, upper, right, lower)

    left = 0
    top = crop_size
    width = left+max_width
    height = top+max_height
    box = (left, top, width, height)
    thumb = thumb.crop(box)
    return thumb


def enden_kirparak_thumb_yarat(width, height, max_width, max_height, thumb):
    resize_ratio = max_height / height
    new_size = (width * resize_ratio, width * resize_ratio)
    thumb.thumbnail(new_size, Image.ANTIALIAS)
    new_width, new_heigth = thumb.size
    crop_size = (new_width - max_width) // 2
    # thumb.crop(left, upper, right, lower)

    left = crop_size
    top = 0
    width = left+max_width
    height = top+max_height
    box = (left, top, width, height)
    thumb = thumb.crop(box)
    return thumb


def enden_genislet_boydan_kirp(width, height, max_width, max_height, thumb):
    new_width, new_heigth, thumb = resize_image(width, height, max_width, max_height, thumb, enden=True)
    crop_size = (new_heigth - max_height) // 2

    left = 0
    top = crop_size
    width = left+max_width
    height = top+max_height
    box = (left, top, width, height)
    thumb = thumb.crop(box)
    return thumb


def boydan_genislet_enden_kirp(width, height, max_width, max_height, thumb):
    new_width, new_heigth, thumb = resize_image(width, height, max_width, max_height, thumb, enden=False)
    crop_size = (new_width - max_width) // 2

    left = crop_size
    top = 0
    width = left+max_width
    height = top+max_height
    box = (left, top, width, height)
    thumb = thumb.crop(box)
    return thumb


def resize_image(width, height, max_width, max_height, thumb, enden):
    if not enden:
        resize_ratio = max_height / height
        new_width = int(width * resize_ratio)
        new_heigth = int(height * resize_ratio)
        new_size = (new_width, new_heigth)
        thumb = thumb.resize(new_size, Image.ANTIALIAS)
        return new_width, new_heigth, thumb
    else:
        resize_ratio = max_width / width
        new_width = int(width * resize_ratio)
        new_heigth = int(height * resize_ratio)
        new_size = (new_width, new_heigth)
        thumb = thumb.resize(new_size, Image.ANTIALIAS)
        return new_width, new_heigth, thumb

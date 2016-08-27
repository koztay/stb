from django.conf import settings
from django.core.files import File
import os
import shutil
from PIL import Image
import random


# bu aşağıdaki fonksiyon çalışmaz. Çünkü lokasyon product olarak gözüküyor.
# universal bir değer döndürecek şekilde düzenlenmeli. Ayrıca
# def thumbnail_location(instance, filename):
#     return "products/%s/thumbnails/%s" % (instance.product.slug, filename)
#
# THUMB_CHOICES = (
#     ("hd", "HD"),
#     ("sd", "SD"),
#     ("micro", "Micro"),
# )


def create_new_thumb(media_path, instance, owner_slug, max_width, max_height):
    filename = os.path.basename(media_path)
    print("filename : %s" % filename)
    thumb = Image.open(media_path)
    width, height = thumb.size
    # size = (max_height, max_width)
    aspect_ratio = width / height

    # width_ratio = width / max_width
    # height_ratio = height / max_height
    #
    # # Eğer aşağıdaki koşul doğru ise resim eninden kırpılacak demektir.
    # if width_ratio > height_ratio:
    #     resize_ratio = max_width / width
    #     new_size = (max_height * resize_ratio, max_width * resize_ratio)
    #     thumb.thumbnail(new_size, Image.ANTIALIAS)
    #     crop_size = (max_height * resize_ratio - height) / 2
    #     box = (crop_size, 0, crop_size, 0)
    #     thumb = thumb.crop(box)
    #

    if width > max_width or height > max_height:
        # eğer 1 den büyükse bu demek ki resmin eni boyundan geniş
        # yani resmin enini max_width 'e kadar küçült boyu uzun kalsın.
        if aspect_ratio > 1:  # resim enden kırpılacak
            resize_ratio = max_height / height
            new_size = (width * resize_ratio, width * resize_ratio)
            thumb.thumbnail(new_size, Image.ANTIALIAS)
            new_width, new_heigth = thumb.size
            crop_size = (new_width-max_width)/2
            # thumb.crop(left, upper, right, lower)
            box = (crop_size, 0, crop_size+max_width, max_height)
            thumb = thumb.crop(box)
        else:  # resim boydan kırpılacak
            resize_ratio = max_width / width
            new_size = (height * resize_ratio, height * resize_ratio)
            thumb.thumbnail(new_size, Image.ANTIALIAS)
            new_width, new_heigth = thumb.size
            crop_size = (new_heigth - max_height) / 2
            # thumb.crop(left, upper, right, lower)
            box = (0, crop_size, 0, crop_size+max_height)
            thumb = thumb.crop(box)
    else:
        # burada stok resim kullanmak lazım. Yani ürün resmi hazırlanıyor vb.
        return False

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

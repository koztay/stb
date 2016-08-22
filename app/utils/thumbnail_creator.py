from django.conf import settings
from django.core.files import File
import os
import shutil
from PIL import Image
import random


# bu aşağıdaki fonksiyon çalışmaz. Çünkü lokasyon product olarak gözüküyor.
# universal bir değer döndürecek şekilde düzenlenmeli. Ayrıca
def thumbnail_location(instance, filename):
    return "products/%s/thumbnails/%s" % (instance.product.slug, filename)

THUMB_CHOICES = (
    ("hd", "HD"),
    ("sd", "SD"),
    ("micro", "Micro"),
)


def create_new_thumb(media_path, instance, owner_slug, max_length, max_width):
    filename = os.path.basename(media_path)
    print("filename : %s" % filename)
    thumb = Image.open(media_path)
    size = (max_length, max_width)
    thumb.thumbnail(size, Image.ANTIALIAS)
    print(thumb)
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

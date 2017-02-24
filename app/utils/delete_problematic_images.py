from products.models import ProductImage, Thumbnail


def delete_all():
    thumb_images_has_no_main = Thumbnail.objects.all()
    images_with_problem = [image for image in thumb_images_has_no_main if not image.main_image.get_image_path()]
    number_of_problematic = len(images_with_problem)
    [image.delete() for image in images_with_problem]
    print("%s problemli thumbnail silindi!" % number_of_problematic)

    thumb_images_has_no_width = Thumbnail.objects.filter(width=None)
    number_of_problematic = len(thumb_images_has_no_width)
    [image.delete() for image in thumb_images_has_no_width]
    print("%s problemli thumbnail silindi!" % number_of_problematic)

    all_product_images = ProductImage.objects.all()
    images_with_problem = [image for image in all_product_images if not image.get_image_path()]
    number_of_problematic = len(images_with_problem)
    [image.delete() for image in images_with_problem]
    print("%s problemli resim silindi!" % number_of_problematic)



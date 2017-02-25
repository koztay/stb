# import pytest
# from mixer.backend.django import mixer
# from django.contrib.auth.models import User
# pytestmark = pytest.mark.django_db
#
#
# class TestProductView:
#
#     def test_model(self):
#         obj = mixer.blend('analytics.ProductView')
#         assert obj.pk == 1, 'Should save an instance'
#
#
# class TestProductViewManager:
#     tst_user = mixer.blend(User)
#     tst_product = mixer.blend('products.Product')
#
#     def test_add_count(self, tst_user, tst_product):
#         obj = mixer.blend('analytics.ProductView')
#         obj.add_count(tst_user, tst_product)
#         assert obj.count == 1





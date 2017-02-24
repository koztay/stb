import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestProduct:
    def test_model(self):
        obj = mixer.blend('products.Product')
        assert obj.pk == 1, 'Should save an instance'


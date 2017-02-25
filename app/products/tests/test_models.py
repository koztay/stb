import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


@pytest.fixture()
def some_product():
    obj = mixer.blend('products.product', title="Test")
    return obj


class TestProduct:
    def test_model(self):
        obj = mixer.blend('products.product')
        assert obj.pk == 1, 'Should save an instance'


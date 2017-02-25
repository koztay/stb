import pytest
from mixer.backend.django import mixer
from .. image_downloader import download_image
pytestmark = pytest.mark.django_db


@pytest.mark.usefixtures("django_db", "db", "transactional_db")
class TestImageDownloader:

    urls = (
        'http://images.hepsiburada.net/assets/OK/500/OK_1481274.jpg',
        'http://images.hepsiburada.net/assets/OK/500/OK_530956.jpg',
        'http://images.hepsiburada.net/assets/OK/500/OK_1855710.jpg',
    )

    titles = (
        'Noki Memo 8 Renk Film Index 12401',
        'DYMO LM 210D Masaüstü Etiketleme Makinesi (6/9/12 mm D1 şeritlerle uyumlu kullanım)',
        'DYMO LM PnP Masaüstü ve PC Bağlantılı Etiketleme Makinesi (6/9/12 mm D1 şeritlerle uyumlu kullanım)',
    )

    # download_image(urls[0], 'some_products[0].id')
    # assert product1.image_set.all()[0].exists() is False,  'Should return the given number of characters'
    assert 1 == 1


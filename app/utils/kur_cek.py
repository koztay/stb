from urllib.request import urlopen
from xml.dom import minidom


def get(currency_name=None):
    url = 'http://www.tcmb.gov.tr/kurlar/today.xml'
    parsed = minidom.parse(urlopen(url))

    # tarih_obj = parsed.getElementsByTagName('Tarih_Date')
    # tarih_value = tarih_obj[0].attributes['Tarih'].value
    # form = '{:30}{:10}{:10}'
    # print('\n' + tarih_value.center(50, '~'), '\n')
    # print(form.format('İSİM', 'ALIŞ', 'SATIŞ'))
    # print('-' * 50)
    tags = ['Isim', 'ForexBuying', 'ForexSelling']
    isim, alis, satis = [parsed.getElementsByTagName(tag) for tag in tags]

    # Aşağıdaki kod tüm kurları yazıdır
    # for i, a, s in zip(isim, alis, satis):
    #     try:
    #         print(form.format(i.firstChild.data,
    #                           a.firstChild.data,
    #                           s.firstChild.data))
    #     except AttributeError:
    #         pass

    for currency, value in zip(isim, satis):
        # print(currency, value)
        # print(currency_name)
        if currency.firstChild.nodeValue == currency_name:
            # print("buldum, buldum !!!!!")
            # print(currency_name)
            # print(currency.firstChild.data)
            return value.firstChild.data

        else:
            print("Kur bulunamadı, lütfen girdiğiniz değeri kontrol edin.")
            # return "Kur bulunamadı, lütfen girdiğiniz değeri kontrol edin." //bunu return edince dongü bitiyor yapma!

# get('EURO')
# get('ABD DOLARI')
# get('abuk')
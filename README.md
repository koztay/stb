
Uygulama notları:
=========

### app altındaki .env dosyası:
app klasörü altındaki .env dosyası [autoenv](https://github.com/kennethreitz/autoenv) sayesinde o klasöre 'cd app' 
yapıldığında .env dosyası içerisinde yeralan environment variable 'larının yüklenmesini sağlıyor. Bu sayede
 
```
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate
``` 

komutlarını verebilir hale geliyoruz.
Benzer şekilde PyCharm environment plugin 'i kullanarak da yine bu .env dosyasını 'Edit Configurations' a ekleyerek
butona basarak lokalde Run/Debug yapabilmeyi sağlıyoruz.
Tabii burada yine bizim şifre vb. dosayalarımız olacağı için gitignore 'a ekleyip remote 'a upload edilmemesini
sağlamalıyız.


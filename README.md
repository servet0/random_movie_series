# random_movie_series

![Ekran görüntüsü 2023-07-07 174126](https://github.com/servet0/random_movie_series/assets/123745302/144ff14f-b5d0-47a2-8be2-408e7c5fea60)

# Django Film Dizi Öneri Web Uygulaması

Bu proje, Django web çatısı kullanılarak geliştirilmiş bir film dizi öneri uygulamasını içerir. Uygulama, kullanıcılara rastgele bir film-dizi önerisinde bulunur ve kullanıcıların IMDb üzerindeki film-dizi sayfalarına yönlendirilmesini sağlar.

## Özellikler

- Rastgele film önerme: Kullanıcılar, film seçeneğini seçerek öneri butonuna tıklayarak rastgele bir film önerisi alabilirler.
- Rastgele dizi önerme: Kullanıcılar, dizi seçeneğini seçerek öneri butonuna tıklayarak rastgele bir dizi önerisi alabilirler.
- IMDb yönlendirmesi: Öneri yapıldığında, kullanıcılar IMDb üzerinde ilgili film-dizi sayfasına yönlendirilirler.

https://github.com/servet0/random_movie_series/assets/123745302/f37cec6f-4f90-403c-b642-47668bb46a3c

## Kurulum

Projeyi çalıştırmak için aşağıdaki adımları takip edin:

1. **Gereksinimleri İndirin:**
    ```bash
    pip install -r requirements.txt
    ```

2. **Veritabanını Migrate Edin:**
    ```bash
    python manage.py migrate
    ```

3. **Yönetici Hesabı Oluşturun:**
    ```bash
    python manage.py createsuperuser
    ```

4. **Sunucuyu Başlatın:**
    ```bash
    python manage.py runserver
    ```

Proje artık `http://localhost:8000` adresinde çalışır durumda olmalıdır. Yönetici paneline `http://localhost:8000/admin` adresinden erişebilirsiniz.

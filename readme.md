# Django Chat App

Bu proyekt django,drf, docker hamda django-channels librarylari orqali yaratildi. Oddiy, sodda ko'rinishdagi chat dasturi

## O'rnatish va ishlatish

Birinchi navbatda venv yaratib olinadi va kerakli librarylarni o'rnatish uchun requriements.txtni o'rnatib olamiz

```bash
pip install -r requriements.txt
```
## Ishga tushirsh uchun redis serverni yoqib olishimiz kerak bo'ladi
```linux
$ docker run --rm -p 6379:6379 redis:7
```
## Redis serveri yonganidan so'ng mana bu komandani kirgizamiz va dastur tayyor
```
py manage.py runserver
```
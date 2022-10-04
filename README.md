# Django REST Framework - Tutorial
Learn how to build REST APIs with Django &amp; the Django Rest Framework.

## 

```python
python manage.py shell
Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from products.models import Product
>>> Product.objects.first().sale_price  
'0.00'
>>> Product.objects.last().sale_price  
'24.00'
```

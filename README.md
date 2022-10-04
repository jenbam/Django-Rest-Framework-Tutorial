# Django REST Framework - Tutorial
Learn how to build REST APIs with Django &amp; the Django Rest Framework.

## Coming soon



```python
python manage.py startapp products

python manage.py makemigrations # Creates model Product, tells Djando about models.py
python manage.py migrate  # make sure that db actually changes

###Django shell

python manage.py shell
>>> from products.models import Product
>>> Product.objects.create(title='Hello world', content='this is amazing', price=0.00)
<Product: Product object (1)>
>>> Product.objects.create(title='Hello Jen', content='Ancona is amazing', price=12.00)
<Product: Product object (2)>
>>> Product.objects.create(title='Hello Bond', content='London is burning', price=30.00)  
<Product: Product object (3)>

>>> Product.objects.all().order_by("?").first()
<Product: Product object (3)>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (2)>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (3)>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (3)>
>>> Product.objects.all().order_by("?").first()
<Product: Product object (3)>

```

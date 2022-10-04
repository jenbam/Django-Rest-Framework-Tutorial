import json
from django.http import JsonResponse

from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        data['id']=model_data.id  # comes in by default
        data['title']=model_data.title
        data['content']=model_data.content
        data['price']=model_data.price
        ## This process is called serialization
        ## We take a model instance (model_data) and turn it into a Python dictionary
        ##..and return JSON to my client

    return JsonResponse(data)
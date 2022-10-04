import json
from django.forms.models import model_to_dict
#from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product

## Using Django Rest Framwork simplifies everything
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    Django Rest Framework View
    """
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        ### we convert the django model instance to a dictionary using a simple built in method
        data = model_to_dict(model_data)
        # data = model_to_dict(model_data, fields=['id', 'title']) # here you can select the fields to display
    return Response(data)

## Using JsonResponse, easier than HttpResponse
""" def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        ### we convert the django model instance to a dictionary using a simple built in method
        data = model_to_dict(model_data)
        # data = model_to_dict(model_data, fields=['id', 'title']) # here you can select the fields to display
    return JsonResponse(data) """


###To do the above in a very hard way by using httpResponse
""" def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        ### we convert the django model instance to a dictionary using a simple built in method
         data = model_to_dict(model_data)
        # data = model_to_dict(model_data, fields=['id', 'title']) # here you can select the fields to display
    # return HttpResponse(data)   #HttpResponse handles text/html data (Content-Type)
    json_data_str = json.dumps(data)
    return HttpResponse(json_data_str, headers={"Content-Type": "application/json"}) """
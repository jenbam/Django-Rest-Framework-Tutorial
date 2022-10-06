from operator import is_
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

# Serializer converts a model instance to a dictionary

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data) # Serialized data, Data validation
    if serializer.is_valid(raise_exception=True):  # add exception to let clients know what they are messing up
        instance = serializer.save()  # This creates an instance. This is the only way to create an instance from the product serializer
        data = serializer.data # This is not a created instance, there is no instance data that has been enriched, that is nothing was ever saved in the database
        print(data)
        return Response(data)
    return Response({"invalid": "not good data"}, status=400) # add this if you don't want clients to know what they are messing 

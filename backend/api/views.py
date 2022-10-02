import json
from django.http import JsonResponse

# request -> HttpRequest -> Django
# print(dir(request))
# request.body [JSON Data]

def api_home(request, *args, **kwargs):
    # print(dir(request))
    print(request.GET) # url query params
    print(request.POST) # 
    body = request.body  # byte string of JSON data
    data = {}
    try:   # Use try block incase body does not have any JSON data
        data = json.loads(body) # This takes in a string of JSON data and returns a Python Dictionary
    except:
        pass
    print(data)
    #print(data.keys())
    # print(request.headers)
    data['params'] = dict(request.GET)
    data['Headers'] = dict(request.headers)
    data['Content_Type'] = request.content_type
    return JsonResponse(data)
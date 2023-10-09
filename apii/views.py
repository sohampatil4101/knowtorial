from django.shortcuts import HttpResponse
from django.http import JsonResponse
from .models import *
from .serializers import ProductSerializer
from .serializers import CartSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.




# API for adding product
@csrf_exempt
def addproduct(request):

    if request.method == 'GET':
        emp = Product.objects.all()
        so = ProductSerializer(emp, many=True)
        return JsonResponse(so.data, safe=False)
    
    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        
        data = Product.objects.last()
        if(data):
            jsonData['id'] = data.id + 1
        else:
            jsonData['id'] = 0

        serializer = ProductSerializer(data= jsonData)
        if serializer.is_valid():
            employee_instance = serializer.save()  
            return JsonResponse(serializer.data, safe=False)
        
        else:
            return JsonResponse(serializer.errors , safe=False)
        

@csrf_exempt
def getproduct(request, pk):

    try:
        data = Product.objects.get(id=pk)
    
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(data)
        return JsonResponse(serializer.data, safe=False)




# add product to cart
@csrf_exempt
def addcart(request):

    if request.method == 'POST':

        jsonData = JSONParser().parse(request)
        serializer = CartSerializer(data= jsonData)
        if serializer.is_valid():
            employee_instance = serializer.save() 
            return JsonResponse(serializer.data, safe=False)
        
        else:
            return JsonResponse(serializer.errors , safe=False)
        
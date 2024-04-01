from .models import Customer
from .serializers import CustomerSerilizer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET"])
def endpoint(request):
    data = ['custname/', 'custdetails/:name']
    return Response(data)

@api_view(["GET", "POST"])
def custname(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerilizer(customers, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        customer = Customer.objects.create(
            name = request.data['name'],
            address = request.data['address'],
            email = request.data['email'],
            contact = request.data['contact']
        )
        serializer = CustomerSerilizer(customer, many=False)
        return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def customer_detail(request, name):
    customer = Customer.objects.get(name = name)
    
    if request.method == "GET":
        serializer =  CustomerSerilizer(customer, many = False)
        return Response(serializer.data)
    
    if request.method == "PUT":
        customer.name = request.data['name'],
        customer.address = request.data['address'],
        customer.email = request.data['email'],
        customer.contact = request.data['contact']
        customer.save()
        serializer =  CustomerSerilizer(customer, many = False)
        return Response(serializer.data)

    if request.method == "DELETE":
        customer.delete()
        return Response("User was deleted")
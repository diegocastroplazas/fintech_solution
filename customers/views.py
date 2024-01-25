from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CustomerSerializer, CustomerBalanceSerializer
from .models import Customer
from django.http import Http404


class CustomersView(APIView):
    """
    List all customer, or create a new customer.
    """

    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerBalanceView(APIView):
    """
    Retrieve a customer balance.
    """

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerBalanceSerializer(customer)
        return Response(serializer.data)
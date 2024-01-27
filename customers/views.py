from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Customer
from .serializers import CustomerBalanceSerializer, CustomerSerializer


class CustomersView(APIView):
    """
    List all customer, or create a new customer.
    """

    permission_classes = [IsAuthenticated]

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

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer = self.get_object(pk)
        serializer = CustomerBalanceSerializer(customer)
        return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CustomerSerializer
from .models import Customer


class CostumersView(APIView):
    """
    List all customer, or create a new customer.
    """

    def get(self, request, format=None):
        costumers = Customer.objects.all()
        serializer = CustomerSerializer(costumers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

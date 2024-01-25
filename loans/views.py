from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Loan

from .serializers import LoanSerializer


class LoansView(APIView):
    """
    List all loans, or create a new loan.
    """

    def get(self, request, format=None):
        loans = Loan.objects.all()
        costumer_external_id = request.query_params.get("costumer_external_id")
        if costumer_external_id:
            loans = loans.filter(customer__external_id=costumer_external_id)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            loan = serializer.save()
            return Response(LoanSerializer(loan).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

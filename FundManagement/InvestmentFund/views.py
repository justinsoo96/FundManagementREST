from rest_framework import generics, status
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import InvestmentFund
from .serializers import InvestmentFundSerializer

# Create your views here.
def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is not None and response.status_code == 500:
        return Response({'error': 'Internal server error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return response

def create_fund(request):
    try:
        new_fund = InvestmentFund.objects.create(**request.data)
        new_fund.save()
        return Response({'message': 'Fund created successfully'}, status=status.HTTP_201_CREATED)
    except ValidationError as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class InvestmentFundListCreate(generics.ListCreateAPIView):
    queryset = InvestmentFund.objects.all()
    serializer_class = InvestmentFundSerializer

class InvestmentFundRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvestmentFund.objects.all()
    serializer_class = InvestmentFundSerializer

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except InvestmentFund.DoesNotExist:
            return Response({'error': 'Fund not found'}, status=status.HTTP_404_NOT_FOUND)

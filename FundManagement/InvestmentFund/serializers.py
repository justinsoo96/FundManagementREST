from rest_framework import serializers
from .models import InvestmentFund

class InvestmentFundSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentFund
        fields = '__all__'

    def validate(self, data):
        # Add custom validation logic here
        if data['fund_performance'] < 0:
            raise serializers.ValidationError("Performance cannot be negative.")
        return data
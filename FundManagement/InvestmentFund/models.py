from django.db import models

# Create your models here.
class InvestmentFund(models.Model):
    fund_id            = models.CharField(max_length=50, unique=True)
    fund_name          = models.CharField(max_length=100)
    fund_manager_name  = models.CharField(max_length=100)
    fund_description   = models.TextField()
    fund_nav           = models.DecimalField(max_digits=20, decimal_places=2) # Assuming NAV is represented as a decimal number
    fund_creation_date = models.DateField(auto_now=True)
    fund_performance   = models.DecimalField(max_digits=5, decimal_places=2) 

    def __str__(self):
        return self.fund_name
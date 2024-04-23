from django.urls import path
from InvestmentFund import views

urlpatterns = [
    path('funds/', views.InvestmentFundListCreate.as_view(), name='fund-list-create'),
    path('funds/<int:pk>/', views.InvestmentFundRetrieveUpdateDestroy.as_view(), name='fund-retrieve-update-destroy'),
]
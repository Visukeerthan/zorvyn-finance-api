from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import FinancialEntryListCreate, FinancialEntryDetail, DashboardSummary

urlpatterns = [
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('entries/', FinancialEntryListCreate.as_view(), name='entry-list'),
    path('entries/<int:pk>/', FinancialEntryDetail.as_view(), name='entry-detail'),
    path('dashboard/', DashboardSummary.as_view(), name='dashboard-summary'),
]
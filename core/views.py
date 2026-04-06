from django.db.models import Sum
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FinancialEntry
from .serializers import FinancialEntrySerializer
from .permissions import RoleBasedPermission

class FinancialEntryListCreate(generics.ListCreateAPIView):
    serializer_class = FinancialEntrySerializer
    permission_classes = [permissions.IsAuthenticated, RoleBasedPermission]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN':
            return FinancialEntry.objects.all()
        return FinancialEntry.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FinancialEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FinancialEntrySerializer
    permission_classes = [permissions.IsAuthenticated, RoleBasedPermission]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'ADMIN':
            return FinancialEntry.objects.all()
        return FinancialEntry.objects.filter(user=user)

# The "Dashboard Math" Endpoint
class DashboardSummary(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        # Logic: Filter records based on role
        qs = FinancialEntry.objects.all() if user.role == 'ADMIN' else FinancialEntry.objects.filter(user=user)

        # The math part: Using Django aggregation
        income = qs.filter(entry_type='INCOME').aggregate(Sum('amount'))['amount__sum'] or 0
        expense = qs.filter(entry_type='EXPENSE').aggregate(Sum('amount'))['amount__sum'] or 0
        
        return Response({
            "total_income": float(income),
            "total_expense": float(expense),
            "net_balance": float(income - expense),
            "recent_activity": qs.values('title', 'amount', 'date')[:5]
        })
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from expenses.models import Expense
from expenses.serializers import ExpenseSerializer


def index(request):
    return HttpResponse("Hi there, it's index.")

class ExpensesViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
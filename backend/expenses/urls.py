from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'expenses', views.ExpensesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

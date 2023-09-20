from django.urls import path
from .views import ProtectedView
urlpatterns = [
    path('prot/', ProtectedView.as_view(), name='ProtectedView'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('add_produto/', views.add_produto, name="add_produto")
]


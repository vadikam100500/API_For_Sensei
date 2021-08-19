from django.urls import path

from . import views

urlpatterns = [
    path('v1/metrics/', views.ShopView.as_view(),)
]

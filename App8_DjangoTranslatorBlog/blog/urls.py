from . import views
from django.urls import path

urlpatterns=[
path('',views.InventoryList.as_view(),name='home'),
#     path('about/',views.AboutView.as_view(),name='about_view'),
    path('<int:pk>/',views.ItemView.as_view(),name='blog_view'),
    
    
]
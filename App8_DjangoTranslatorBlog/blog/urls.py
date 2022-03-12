from . import views
from django.urls import path

urlpatterns=[
path('',views.ItemView,name='item_detail'),
    # path('tran/',views.AboutView.as_view(),name='about_view'),
    path('<int:bucin>/',views.InventoryDetail,name='inventory_detail'),
    
    
]
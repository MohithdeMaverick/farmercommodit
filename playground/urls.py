from django.urls import path
from . import views

urlpatterns=[
    path('',views.hello),
    path('login/',views.register_page,name='login'),
    path('farmer/',views.farmer_page,name='farmer'),
    path('vendor/',views.vendor_page,name='vendor'),
    path('customer/',views.customer_page,name='customer'),
    path('delete/<int:id>/', views.delete_submission, name='delete_submission')
]
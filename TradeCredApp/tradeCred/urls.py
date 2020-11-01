from django.urls import path

from . import views

app_name = 'tradeCred'

urlpatterns = [
    path('', views.index, name='index'),
    path('upload_vendor_data/', views.Upload_data.as_view(), name='upload_vendor_data'),
    path('see_vendor_data/', views.See_Vendors_data.as_view(), name='see_vendor_data'),
    path('delete_data/', views.Delete_data.as_view(), name='delete_data'),
]

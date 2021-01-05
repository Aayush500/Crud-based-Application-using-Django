from django.urls import path
from . import views


urlpatterns = [
    path('', views.save_data, name= 'save_data'),
    path('delete/<int:delete_id>/', views.delete, name= 'delete'),
    path('edit/<int:my_id>/', views.edit, name = 'edit')
]

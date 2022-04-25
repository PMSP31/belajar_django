from django.urls import path
from .views import ListView, DeleteView, SosmedFormView

app_name = 'sosmed'
urlpatterns = [
    path('', ListView.as_view(), name='index'),
    path('create/', SosmedFormView.as_view(), name='create'),
    path('update/<int:update_id>', SosmedFormView.as_view(mode='update'), name='update'),
    path('delete/<int:delete_id>', DeleteView.as_view(), name='delete'),
]
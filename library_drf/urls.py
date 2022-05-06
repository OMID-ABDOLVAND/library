
from django.urls import path
from library_drf import views
urlpatterns = [
    path('list/', views.ListView.as_view(), name='list_book'),
    path('detail/<pk>/', views.DetailView.as_view(), name='detail_book'),
]
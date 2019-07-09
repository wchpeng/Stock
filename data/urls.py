from django.urls import path
from data import views

urlpatterns = [
    path('info/<slug:code>/', views.StockInfoView.as_view(), name='stock_info_html'),
    path('list', views.StockListView.as_view(), name='stock_list_html'),
]
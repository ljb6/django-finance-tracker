from django.contrib import admin
from django.urls import path
from app_finance_tracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tables/', views.tables, name='table_list'),
    path('delete-tables', views.delete_tables, name='delete_tables'),
    path('delete-line', views.delete_line, name='delete_line'),
    path('table/<int:id>', views.table, name='table'),
    path('add-transaction', views.add_transaction, name='add_transaction')
]
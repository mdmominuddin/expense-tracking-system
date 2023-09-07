from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('enter-contribution/', views.enter_contribution, name='enter_contribution'),
    path('enter-expense/', views.enter_expense, name='enter_expense'),
    path('summary/', views.summary, name='summary'),
    path('month-wise-audit/', views.month_wise_audit, name='month_wise_audit'),
    path('category-wise-audit/', views.category_wise_audit, name='category_wise_audit'),
    path('item-wise-audit/', views.item_wise_audit, name='item_wise_audit'),
]

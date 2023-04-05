from django.contrib import admin
from django.urls import path

from .views import StudentCreateView, ThankyouTemplateView, StudentDetailView, StudentUpdateView, ThanksUpdateTemplateView, StudentDeleteView, DeleteTemplateView

urlpatterns = [
    path('create/', StudentCreateView.as_view(), name='create-student'),
    path('thankyou/', ThankyouTemplateView.as_view(), name='thankyou-page'),
    path('studetail/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),

    path('update/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('thanksupdate/', ThanksUpdateTemplateView.as_view(), name='thankyou-update'),
    
    path('delete/<int:pk>', StudentDeleteView.as_view(), name='student-delete'),
    path('delete/', DeleteTemplateView.as_view(), name='delete-student-page'),
]
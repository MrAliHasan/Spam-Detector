# spam_detector/spamapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict_spam, name='predict_spam'),
]

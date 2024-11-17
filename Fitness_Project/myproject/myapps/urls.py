from django.urls import path
from myapps import views
urlpatterns = [
    path('signin',views.signin),
    path('signup',views.signup)
]

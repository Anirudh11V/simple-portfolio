from django.urls import path, include
from cvapp import views



urlpatterns = [
    # cvapp urls....................................
    path('', views.index, name='inx'),
    path('home/', views.home, name='homee'),
    path('thnx/', views.thanks, name='thnx'),

    # cvapp url end .........................................


]



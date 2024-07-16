from django.urls import path, include
from cvapp import views

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
)

urlpatterns = [
    # cvapp urls....................................
    path('', views.index, name='inx'),
    path('home/', views.home, name='homee'),
    path('thnx/', views.thanks, name='thnx'),

    # cvapp url end .........................................


    # DRF urls.................................................................................
    path('end/',views.endpoint,name='end'),
    path('comments/',views.comments,name='comments'),
    path('comment_details/<str:Name>/',views.comment_details, name='comment_detail'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),

    # DRF url end ..............................................................................

]


urlpatterns = format_suffix_patterns(urlpatterns)
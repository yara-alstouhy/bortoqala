from django.urls import path
from .views import testApiView, UserApiView

urlpatterns = [
    path('', testApiView.as_view()),
    path('user/', UserApiView.as_view())

]

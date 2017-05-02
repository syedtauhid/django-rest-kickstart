from django.conf.urls import url

from api_call.rest_api import views

urlpatterns = [
    url(r'^name/$', views.NameListAPIView.as_view()),
]

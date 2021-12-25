from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^School$',views.schoolApi),
    url(r'^School/([0-9]+)$',views.schoolApi)
]


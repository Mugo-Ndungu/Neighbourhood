from django.conf.urls import url
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.home,name='home'),
]

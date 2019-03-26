from django.conf.urls import url, include
from . import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='register'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^post/', views.post, name='post'),
    url(r'^estate/', views.estate, name='estate'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^profiles/(\d+)', views.profiles, name='profiles'),
    url(r'^create/', views.create, name='create'),
    url(r'^business/', views.business, name='business'),
    url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    url(r'^login/$', auth_views.LoginView.as_view(
        template_name='registration/login.html'), name='login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

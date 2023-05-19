from django.contrib import admin
from django.urls import path, include
from phone import settings
from . import views
#from . views import home
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.add, name="home"),
    path('signup', views.signup , name="signup"),
    path('signin', views.signin , name="signin"),
    path('signout', views.signout , name="signout"),
    #path('add', views.add, name="add"),
    ]

urlpatterns += staticfiles_urlpatterns()

urlpatterns = urlpatterns+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)
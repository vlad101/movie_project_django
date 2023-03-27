from django.contrib import admin
from django.urls import include, path
from movie_app import views as movie_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', movie_views.home, name='home'),
    path('movie/', include('movie_app.urls')),
]

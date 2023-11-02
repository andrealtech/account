from django.contrib import admin
from django.urls import path
from marca.views import marcas_view
from accounts.views import login_view, register_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('marcas/', marcas_view, name='marcas'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

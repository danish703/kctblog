
from django.contrib import admin
from django.urls import path
from .views import blog,contact,about,home,register,signin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home),
    path('admin/', admin.site.urls),
    path('blog/',blog),
    path('about/',about),
    path('contact/',contact),
    path('register/',register,name='register'),
    path('login/',signin,name='signin'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

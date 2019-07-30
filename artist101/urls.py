
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import main.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name='index'),
    path('mypage/', main.views.mypage, name="mypage"),
    path('makeup/', main.views.makeup, name="makeup"),
    path('beautynail/', main.views.beautynail, name="beautynail"),
    #path('login/', accounts.views.login, name="login"),
    path('about/', main.views.about, name="about"),
    path('services/', main.views.services, name="services"),
    #path('join/', accounts.views.join, name="join"),
    path('accounts/', include('accounts.urls')),
    path('new/', main.views.new, name="new"),
    path('create/', main.views.create, name='create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('razer/audio',views.razer_audio, name = "razer_audio"),
    path('razer/keyboard',views.razer_keyboard,name = "razer_keyboard"),
    path('razer/mice',views.razer_mice, name = "razer_mice"),
    path('register', views.register, name='register'),
    path('dead', views.dead, name = "dead"),
    path('test', views.test, name = "test"),
    path(r'^productaudio/?P<product_name>\w+/$', views.Products, name = "productaudio"),
    path(r'^productmice/?P<product_name>\w+/$', views.Products, name="productmice"),
    path(r'^productkeyboard/?P<product_name>\w+/$', views.Products, name="productkeyboard"),
]

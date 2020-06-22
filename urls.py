import views
from django.urls import path


urlpatterns = [
    path('', views.hello),
    path('bye', views.bye),
    path('counter', views.counter)
]

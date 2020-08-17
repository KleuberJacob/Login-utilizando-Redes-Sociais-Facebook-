from django.urls import path, include
from django.contrib.auth import views as auth_views  # auth_views é um apelido para views
from .views import IndexView, LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('', IndexView.as_view(), name='index'),
]

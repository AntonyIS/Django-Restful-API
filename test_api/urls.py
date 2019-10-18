from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('languages.urls')),
    path('api-auth/',include(r'rest_framework.urls')),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
]

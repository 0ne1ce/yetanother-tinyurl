from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from links import views

router = DefaultRouter()
router.register(r'urls', views.URLViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^(?P<tinyurl>[A-Za-z0-9]{10})/$', views.redirect_view, name='redirect'),
    path('api/v1/', include(router.urls)),
    path('api/v1/<str:tinyurl>/stats/', views.view_redirect_statistics, name='view_redirect_statistics'),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('redoc/', TemplateView.as_view(template_name='redoc.html'), name='redoc')
]

import debug_toolbar
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

schema_view = get_schema_view(
    openapi.Info(
        title="Order List",
        default_version="v1",
        description="This is documentation for backend API",
        terms_of_service="http://mywebsite.com/policies/",
        contact=openapi.Contact(email="mohammadbaharloo96@gmail.com"),
        license=openapi.License(name="Backend License"),
    ),
    public=True,
    permission_classes=(AllowAny,),  
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('api/v1/',include('api.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api-auth/', include('rest_framework.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
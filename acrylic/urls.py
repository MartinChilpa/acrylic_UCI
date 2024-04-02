from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from drf_spectacular.views import SpectacularAPIView

API_VERSION = 'v1'


urlpatterns = [
    path('admin/', admin.site.urls),

    # API urls
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    

    path(f'api/{API_VERSION}/', include([
        # JWT authentication
        path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

        path('', include('artist.api.urls')),

        # API social auth
        #path('auth/social/', include('rest_framework_social_oauth2.urls')),
        #path('auth/', include('rest_social_auth.urls_jwt_pair')),

        # Accounts
        #path('accounts/profile/', profile, name='profile'),
        # Registration
        #path('accounts/', include('rest_registration.api.urls')),
    ])),
]


#router = routers.SimpleRouter()
#router.register(f'api/{API_VERSION}/library/category', library_views.CategoryViewSet, basename='category')



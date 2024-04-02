from django.urls import include, path
from rest_framework import routers

from artist.api import views

app_name = 'artist'


router = routers.DefaultRouter()
router.register('artists', views.ArtistViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

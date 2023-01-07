from django.urls import path,include
from rest_framework import routers
from movies.views import movieview

router = routers.DefaultRouter()
router.register('movies', movieview)

urlpatterns = [
    path('', include(router.urls)),
]

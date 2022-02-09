from django.urls import path, include
from rest_framework import routers

from . import views
from . views import UsersetViews

router = routers.DefaultRouter()
# router.register(r'usersets', views.UsersetViewSet)

urlpatterns = [
    path('', include(router.urls)),     #
    path('usersets/', UsersetViews.as_view()),
    path('usersets/<int:id>/', UsersetViews.as_view()),
]

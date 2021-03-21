from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'groups', GroupViewSet, basename='Group')
router.register(r'members', MembershipViewSet, basename='MemberShip')

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

# creating router object
router=DefaultRouter()
# register UserViewSet with Router
router.register('user', views.UserViewset, basename='user')
router.register('product', views.ProductViewset, basename='product')
router.register('category', views.CategoryViewset, basename='category')

urlpatterns = [
    path('',include(router.urls))

]
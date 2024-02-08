from rest_framework.routers import DefaultRouter
from myapp.views import ProductViewset

router=DefaultRouter()

router.register('product',ProductViewset,basename='product')

urlpatterns=router.urls

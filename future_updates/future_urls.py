# from rest_framework_nested import routers
# from django.conf import settings
# from django.conf.urls.static import static
#from .views import CustomerViewSet, OrderViewSet, ProductImageViewSet, ProductViewSet, ReviewViewSet

# router = routers.DefaultRouter()
# router.register('products', ProductViewSet)
# router.register('customers', CustomerViewSet)
# router.register('orders', OrderViewSet, basename='orders')

# products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
# products_router.register('images', ProductImageViewSet, basename='product-images')
# products_router.register('reviews', ReviewViewSet, basename='product-reviews')

# urlpatterns = router.urls + products_router.urls
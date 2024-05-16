from django.urls import path, include
from rest_framework_nested import routers
from .views import CartViewSet, CartItemViewSet

router = routers.DefaultRouter()
router.register('carts', CartViewSet)

nested_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
nested_router.register('items', CartItemViewSet, basename='cart-items')

# Define the urlpatterns
urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]

urlpatterns += [
    path('carts/<int:pk>/checkout/', CartViewSet.as_view({'post': 'checkout'}), name='cart-checkout'),
]

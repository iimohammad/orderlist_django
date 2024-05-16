from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from userauths import views as userauth_views
from store import views as store_views
from rest_framework.routers import DefaultRouter
from vendor import views as vendor_views
from store import views as store_views
from finance import views as finance_views
from membership import views as membership_views


router = DefaultRouter()
router.register('user/profiles', userauth_views.ProfileViewSet)

# Vendor
router.register('vendors/vendors', vendor_views.VendorViewSet)
router.register('vendors/brands', vendor_views.BrandViewSet)
router.register('vendors/collections', vendor_views.CollectionViewSet)
router.register('vendors/parts', vendor_views.PartViewSet)
router.register('vendors/order-responses', vendor_views.OrderResponseViewSet)


# Store
router.register('store/vendees', store_views.VendeeViewSet)
router.register('store/orders', store_views.OrderViewSet)
router.register('store/order-items', store_views.OrderItemViewSet)
router.register('store/selected-vendors', store_views.SelecteVendorViewSet)


#finance
router.register('finance/PurchaseOrder', finance_views.PurchaseOrderViewSet, basename='PurchaseOrder')
router.register('finance/PurchaseOrderItem', finance_views.PurchaseOrderItemViewSet, basename='PurchaseOrderItem')

#membership
router.register('membership/memberships', membership_views.MembershipViewSet)

urlpatterns = [
    # path('user/', include('rest_framework.urls')),
    # path('user/token/', userauth_views.MyTokenObtainPairView.as_view()),
    # path('user/token/refresh/', TokenRefreshView.as_view()),
    path('user/register/', userauth_views.RegisterView.as_view()),
    path('user/password-reset/<email>/', userauth_views.PasswordResetEmailVerify.as_view()),
    path('user/password-change/', userauth_views.PasswordChangedView.as_view()),
    path('user/email-verification/<str:email>/', userauth_views.Email_Verification.as_view()),
    path('user/phone-verification/', userauth_views.Phone_Verification_send_sms.as_view()),
    path('user/phone-verification-code/', userauth_views.Phone_Verification.as_view()),
] + router.urls




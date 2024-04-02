from django.urls import path
from. import views

app_name='orders'

urlpatterns=[
    path('cartview/', views.CartView.as_view(), name='cart_view'),
    path('addcart/<int:product_id>',views.CartAddView.as_view(), name='add_cart'),
    path('removecart/<int:product_id>', views.RemoveCartView.as_view(), name='remove_cart'),
    path('createorder/', views.CreateOrderView.as_view(), name='create_order'),
    path('detail/order/<int:order_id>', views.DetailOrderView.as_view(), name='detail_order'),
    path('senderdetail/<int:order_id>',views.SenderinfoView.as_view(), name='sender_info'),
    path('apply/coupon/<int:order_id>',views.ApplycouponView.as_view(), name='apply_coupon'),
    path('order/final/<int:order_id>', views.OrderfinalView.as_view(),name='order_final')

    
]
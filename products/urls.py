from django.urls import path
from. import views

app_name='products'

urlpatterns=[
    path('', views.productview.as_view(), name='products'),
    path('category/<slug:category_slug>', views.productview.as_view(), name='category'),
    path('detail/<int:pk>/', views.productDetail.as_view(), name='products_detail'),
    path('sendreply/<int:product_id>/<int:comment_id>/',views.createreply.as_view(), name='reply'),


   
]
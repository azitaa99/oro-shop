from django.urls import path
from. import views

app_name='accounts'

urlpatterns=[
    path('register/', views.UserRegister.as_view(), name='register'),
    path('login/', views.Userlogin.as_view(), name='login'),
    path('login/<int:code_id>', views.Userlogin.as_view(), name='login_with_code'),
    path('login/sms/',views.UserLoginCode.as_view(), name='login_sms'),
    path('logout/', views.Userlogout.as_view(), name='logout'),
    path('reset/', views.userpasswordresetView.as_view(), name='pass_reset'),
    path('reset/done', views.userpasswordresetdoneview.as_view(), name='pass_reset_done'),
    path('confirm/<uidb64>/<token>', views.userpasswordresetconfirmview.as_view(), name='pass_reset_confirm'),
    path('confirm/complete', views.userpasswordresetcompleteview.as_view(), name='pass_reset_complete'),

]
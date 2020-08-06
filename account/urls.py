from django.conf.urls import url
from .views import *
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.views import ObtainJSONWebToken
from valentisHealth.backends import CustomJWTSerializer


urlpatterns = [
    url('^log-in/$', LoginPage.as_view(), name='login'),
    url(r'^pdf/', print_pdf, name='print'),
    url(r'^logout/', Logout.as_view(), name='logout'),
    url(r'^admin/adduser/', AddUser.as_view(), name='adduser'),
    url(r'^activate/(?P<email>[0-9A-Za-z_@\-.]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    url(r'^workflow', Workflow.as_view(), name='workflow'),
    url(r'^resend_activation/', ResendActivation.as_view(), name='resend_activation'),
    url(r'^reset_password/', ResetPassword.as_view(), name='reset_password'),
    url(r'^change_password/', ChangePassword.as_view(), name='change_password'),

]

urlpatterns += [
    url(r'^api/auth/token', ObtainJSONWebToken.as_view(serializer_class=CustomJWTSerializer)),
    url(r'^api/auth/refresh/', refresh_jwt_token),
    url(r'^api/auth/verify/', verify_jwt_token)
]
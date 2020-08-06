from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'message', api.MessageViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Message
    # url(r'^$', views.MessageListView.as_view(), name='workflow_message_list'),
    url(r'^$', views.MessageCreateView.as_view(), name='workflow_message_list'),
    url(r'^new/$', views.MessageCreateView.as_view(), name='workflow_message_create'),
)


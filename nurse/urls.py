from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'nurse', api.modelsViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for models
    # url(r'^nurse/list/$', views.ModelsListView.as_view(), name='nurse_triage_list'),
    url(r'^nurse/', views.NurseLandingView.as_view(), name='nurse_landing'),
    url(r'^create/(?P<patient_no>\S+)/$', views.NurseCreateView.as_view(), name='nurse_triage_create'),
    url(r'^nurse/detail/(?P<slug>\S+)/$', views.NurseDetailView.as_view(), name='nurse_triage_detail'),
    url(r'^nurse/update/(?P<slug>\S+)/$', views.NurseUpdateView.as_view(), name='nurse_triage_update'),
)


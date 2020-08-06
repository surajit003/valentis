from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'tests', api.LabResultsViewSet)
router.register(r'radiology', api.RadiologyResultViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for tests
    url(r'^labs/$', views.LabsLanding.as_view(), name='tests_labs_list'),
    url(r'^labs/create/$', views.LabsCreateView.as_view(), name='tests_labs_create'),
    url(r'^labs/detail/(?P<slug>\S+)/$', views.LabsDetailView.as_view(), name='tests_labs_detail'),
    url(r'^labs/update/(?P<slug>\S+)/$', views.LabsUpdateView.as_view(), name='tests_labs_update'),
)

urlpatterns += (
    # urls for radiology
    url(r'^radiology/$', views.RadiologyListView.as_view(), name='pythonradiology_list'),
    url(r'^radiology/create/$', views.RadiologyCreateView.as_view(), name='tests_radiology_create'),
    url(r'^radiology/detail/(?P<slug>\S+)/$', views.RadiologyDetailView.as_view(), name='tests_radiology_detail'),
    url(r'^radiology/update/(?P<slug>\S+)/$', views.RadiologyUpdateView.as_view(), name='tests_radiology_update'),
)

urlpatterns += (
    # urls for RadiologyResult
    url(r'^radiologyresult/$', views.RadiologyResultListView.as_view(), name='radiologyresult_list'),
    url(r'^radiologyresult/new/(?P<patient_no>\S+)/$', views.RadiologyVisitView.as_view(), name='radiologyresult_create'),
    url(r'^radiologyresult/detail/(?P<slug>\S+)/$', views.RadiologyResultDetailView.as_view(), name='radiologyresult_detail'),
    url(r'^radiologyresult/update/(?P<slug>\S+)/$', views.RadiologyResultUpdateView.as_view(), name='radiologyresult_update'),
)

urlpatterns += (
    # urls for LabResults
    url(r'^labresultslist/$', views.LabResultsListView.as_view(), name='labresults_list'),
    # url(r'^labs/(?P<triage_id>\S+)/$', views.Labs.as_view(), name='labs_list'),
    url(r'^labresults/new/(?P<patient_no>\S+)/$', views.LabsVisitView.as_view(), name='labresult_create'),
    url(r'^labresults/detail/(?P<slug>\S+)/$', views.LabResultsDetailView.as_view(), name='labresults_detail'),
    url(r'^labresults/update/(?P<slug>\S+)/$', views.LabResultsUpdateView.as_view(), name='labresults_update'),
)
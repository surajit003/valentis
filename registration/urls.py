from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'patients', api.modelsViewSet)
router.register(r'allergies', api.allergiesviewset)
router.register(r'county', api.countyviewset)
router.register(r'medicationhistory', api.medicationhistoryviewset)
router.register(r'insurance', api.insurancecompanyviewset)




urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for models
    url(r'^$', views.LandingView.as_view(), name='registration_search'),
    url(r'^patient/create/$', views.PatientCreateView.as_view(), name='registration_patient_create'),
    url(r'^patient/existing/(?P<patient_no>\S+)/$', views.PatientDetailView.as_view(), name='registration_patients_detail'),
    url(r'^patient/update/(?P<patient_no>\S+)/$', views.PatientUpdateView.as_view(), name='registration_update'),
    url(r'^patient/send-to-triage/(?P<patient_no>\S+)/$', views.SendToTriageView.as_view(), name='registration_sent_to_triage'),
)


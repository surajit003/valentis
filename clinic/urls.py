from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'patientvisit', api.PatientVisitViewSet)
router.register(r'icd10', api.DiagnosisViewSet)
router.register(r'radiologytests', api.RadiologyResultsViewSet)




urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for patientVisit
    url(r'^patientvisit/$', views.PatientVisitListView.as_view(), name='clinic_patientvisit_list'),
    url(r'^clinic_report/(?P<visit_id>\S+)/$', views.ClinicReport.as_view(), name='clinic_report'),
    url(r'^patientvisit/doctor/(?P<patient_no>\S+)/$', views.DoctorVisit.as_view(), name='doctor_visit'),
    url(r'^patientvisit/close/(?P<patient_no>\S+)/$', views.Close.as_view(), name='close_visit'),
    url(r'^patientvisit/create/$', views.PatientVisitCreateView.as_view(), name='clinic_patientvisit_create'),
    url(r'^patientvisit/detail/(?P<slug>\S+)/$', views.PatientVisitDetailView.as_view(), name='clinic_patientvisit_detail'),
    url(r'^patientvisit/update/(?P<slug>\S+)/$', views.PatientVisitUpdateView.as_view(), name='clinic_patientvisit_update'),
)


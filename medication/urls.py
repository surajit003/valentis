from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'medication', api.MedicationViewSet)
router.register(r'MyDawa', api.myDawaModelSet)
router.register(r'MyDawaPrescriptions', api.myDawaPrescriptionsModelSet)



urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
    #url(r'^api/v2/', include(router.urls)),

)

urlpatterns += (
    # urls for models
    url(r'^medication/$', views.MedicationListView.as_view(), name='medication_models_list'),
    url(r'^prescription-pdf/$', views.PrescriptionPdf.as_view(), name='medication_prescription_pdf'),
    url(r'^search/$', views.MedicationSearchView.as_view(), name='medication_models_search'),
    url(r'^medication/new/(?P<patient_no>\S+)/$', views.MedicationCreateView.as_view(), name='medication_models_create'),
    url(r'^medication/detail/(?P<slug>\S+)/$', views.MedicationDetailView.as_view(), name='medication_models_detail'),
    url(r'^medication/update/(?P<slug>\S+)/$', views.MedicationUpdateView.as_view(), name='medication_models_update'),
)


from django.conf.urls import url, include
from rest_framework import routers
from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'member_info', api.member_infoViewSet)
router.register(r'member_benefits', api.member_benefitsViewSet)
router.register(r'member_anniversary', api.member_anniversaryViewSet)
router.register(r'member_acceptance', api.member_acceptanceViewSet)
router.register(r'principal_applicant', api.principal_applicantViewSet)
router.register(r'pre_authorization', api.pre_authorizationViewSet)
router.register(r'provider', api.providerViewSet)
router.register(r'cash', api.cashViewSet)
router.register(r'memberinfosanlam', api.memberinfosanlamviewset)

# router.register(r'update', views.UpdateLimit.as_view(), base_name='benefits_limit_update')


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for member_info
    url(r'^member_info/$', views.member_infoListView.as_view(), name='payments_member_info_list'),
    url(r'^member_info/create/$', views.member_infoCreateView.as_view(), name='payments_member_info_create'),
    url(r'^member_info/detail/(?P<slug>\S+)/$', views.member_infoDetailView.as_view(), name='payments_member_info_detail'),
    url(r'^member_info/update/(?P<slug>\S+)/$', views.member_infoUpdateView.as_view(), name='payments_member_info_update'),
    url('^member_info/(?P<member_id>.+)/$', views.getUser.as_view()),
    url('^member_benefits/(?P<member_id>.+)/$', views.getBenefits.as_view()),
    url('^member_anniversary/(?P<member_id>.+)/$', views.getAniversary.as_view()),
    url('^providers/(?P<member_id>.+)/$', views.getBenefits.as_view()),
    url(r'^update/(?P<slug>\S+)/$', views.UpdateLimit.as_view(), name='benefits_limit_update'),
)

urlpatterns += (
    # urls for member_benefits
    url(r'^member_benefits/$', views.member_benefitsListView.as_view(), name='payments_member_benefits_list'),
    url(r'^member_benefits/create/$', views.member_benefitsCreateView.as_view(), name='payments_member_benefits_create'),
    url(r'^member_benefits/detail/(?P<slug>\S+)/$', views.member_benefitsDetailView.as_view(), name='payments_member_benefits_detail'),
    url(r'^member_benefits/update/(?P<slug>\S+)/$', views.member_benefitsUpdateView.as_view(), name='payments_member_benefits_update'),
)

urlpatterns += (
    # urls for member_anniversary
    url(r'^member_anniversary/$', views.member_anniversaryListView.as_view(), name='payments_member_anniversary_list'),
    url(r'^member_anniversary/create/$', views.member_anniversaryCreateView.as_view(), name='payments_member_anniversary_create'),
    url(r'^member_anniversary/detail/(?P<slug>\S+)/$', views.member_anniversaryDetailView.as_view(), name='payments_member_anniversary_detail'),
    url(r'^member_anniversary/update/(?P<slug>\S+)/$', views.member_anniversaryUpdateView.as_view(), name='payments_member_anniversary_update'),
)

urlpatterns += (
    # urls for member_acceptance
    url(r'^member_acceptance/$', views.member_acceptanceListView.as_view(), name='payments_member_acceptance_list'),
    url(r'^member_acceptance/create/$', views.member_acceptanceCreateView.as_view(), name='payments_member_acceptance_create'),
    url(r'^member_acceptance/detail/(?P<slug>\S+)/$', views.member_acceptanceDetailView.as_view(), name='payments_member_acceptance_detail'),
    url(r'^member_acceptance/update/(?P<slug>\S+)/$', views.member_acceptanceUpdateView.as_view(), name='payments_member_acceptance_update'),
)

urlpatterns += (
    # urls for principal_applicant
    url(r'^principal_applicant/$', views.principal_applicantListView.as_view(), name='payments_principal_applicant_list'),
    url(r'^principal_applicant/create/$', views.principal_applicantCreateView.as_view(), name='payments_principal_applicant_create'),
    url(r'^principal_applicant/detail/(?P<slug>\S+)/$', views.principal_applicantDetailView.as_view(), name='payments_principal_applicant_detail'),
    url(r'^principal_applicant/update/(?P<slug>\S+)/$', views.principal_applicantUpdateView.as_view(), name='payments_principal_applicant_update'),
)

urlpatterns += (
    # urls for pre_authorization
    url(r'^pre_authorization/$', views.pre_authorizationListView.as_view(), name='payments_pre_authorization_list'),
    url(r'^ajax_pre_authorization/$', views.AjaxPreAuthorizationSearch.as_view(), name='payments_ajax_pre_authorization'),
    url(r'^pre_authorization/search/$', views.PreAuthorizationSearch.as_view(), name='payments_pre_authorization_search'),
    url(r'^pre_authorization/create/$', views.pre_authorizationCreateView.as_view(), name='payments_pre_authorization_create'),
    url(r'^pre_authorization/new/(?P<slug>\S+)/$', views.PreAuthorizationCreateView.as_view(), name='payments_pre_authorization_new'),
    url(r'^pre_authorization/nnew/(?P<slug>\S+)/$', views.PPreAuthorizationCreateView.as_view(), name='ppayments_pre_authorization_new'),
    url(r'^search_member/$', views.searchView.as_view(), name='payments_search_member'),
    url(r'^pre_authorization/detail/(?P<slug>\S+)/$', views.pre_authorizationDetailView.as_view(), name='payments_pre_authorization_detail'),
    url(r'^pre_authorization/print/(?P<slug>\S+)/$', views.PreAuthorizationPrintView.as_view(), name='payments_pre_authorization_print'),
    url(r'^pre_authorization/update/(?P<slug>\S+)/$', views.pre_authorizationUpdateView.as_view(), name='payments_pre_authorization_update'),
)

urlpatterns += (
    # urls for provider
    url(r'^provider/$', views.providerListView.as_view(), name='payments_provider_list'),
    url(r'^provider/create/$', views.providerCreateView.as_view(), name='payments_provider_create'),
    url(r'^provider/detail/(?P<slug>\S+)/$', views.providerDetailView.as_view(), name='payments_provider_detail'),
    url(r'^provider/update/(?P<slug>\S+)/$', views.providerUpdateView.as_view(), name='payments_provider_update'),
)

urlpatterns += (
    # urls for cash
    url(r'^cash/$', views.cashListView.as_view(), name='payments_cash_list'),
    url(r'^cash/create/$', views.cashCreateView.as_view(), name='payments_cash_create'),
    url(r'^cash/detail/(?P<slug>\S+)/$', views.cashDetailView.as_view(), name='payments_cash_detail'),
    url(r'^cash/update/(?P<slug>\S+)/$', views.cashUpdateView.as_view(), name='payments_cash_update'),

)




"""dj110 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from account.views import Home
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'ValentisHealth Administration'
admin.site.site_title = 'ValentisHealth Administration'

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^registration/', include('registration.urls')),
                  url(r'^nurse/', include('nurse.urls')),
                  url(r'^medication/', include('medication.urls')),
                  url(r'^tests/', include('tests.urls')),
                  url(r'^clinic/', include('clinic.urls')),
                  url(r'^payments/', include('payments.urls')),
                  url(r'^account/', include('account.urls')),
                  url(r'^workflow/', include('workflow.urls')),
                  url(r'^$', include('registration.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from re import compile
from urllib.parse import urlencode

from django.http import HttpResponseRedirect
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from valentisHealth import settings

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware(MiddlewareMixin):

    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
    you can copy from your urls.py).

    Requires authentication middleware and template context processors to be
    loaded. You'll get an error if they aren't.
    """

    def api_requests(self, request):
        path = request.path.split('/')
        for each in path:
            if each == 'api':
                return None
        pass

    def process_request(self, request):
        assert hasattr(
            request, 'user'), "The Login Required middleware requires authentication middleware to be installed. Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.auth.middlware.AuthenticationMiddleware'. If that doesn't work, ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes 'django.core.context_processors.auth'."
        #avoid using the mail authentication for api request : this will be handled using tokens
        path = request.path.split('/')
        for each in path:
            if each == 'api':
                return None

        if not request.user.is_authenticated() \
                and not request.path.startswith('/account/activate/')\
                and not request.path.startswith('/account/api-token-auth/'):
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                params = request.GET.copy()
                params['next'] = request.path
                return HttpResponseRedirect(settings.LOGIN_URL + '?' + urlencode(params))


class ForceLogoutMiddleware(object):

    """
    Middleware that forces a user to be logged out if they are deactivated, or
    their user role is changed.
    """

    def process_request(self, request):
        if request.user.is_authenticated() \
                and request.user.force_logout_date and \
                request.user.last_login < request.user.force_logout_date:
            logout(request)
            return HttpResponseRedirect(settings.LOGIN_URL)


class SessionIdleTimeout:
    def process_request(self, request):
        if request.user.is_authenticated():
            current_datetime = datetime.datetime.now()
            if ('last_login' in request.session):
                last = (current_datetime - request.session['last_login']).seconds
                if last > settings.SESSION_IDLE_TIMEOUT:
                    logout(request)
                return HttpResponseRedirect(settings.LOGIN_URL)
            else:
                request.session['last_login'] = current_datetime
        return None


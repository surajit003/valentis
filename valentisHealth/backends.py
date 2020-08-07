from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from account.models import CustomUser
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from django.utils.translation import ugettext as _
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from registration.serializers import PatientSerializer
from registration.models import Patient

User = get_user_model()

class EmailAuthBackend(ModelBackend):
    """
    Email Authentication Backend

    Allows a user to sign in using an email/password pair rather than
    a username/password pair.
    """
    @classmethod
    def authenticate(cls,username=None, password=None, **kwargs):
        """ Authenticate a user based on email address as the user name. """
        try:
            user = CustomUser.objects.get(email=username)
            print('Abc',user)
            if user.check_password(password):
                print('entered here')
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """ Get a User object from the user_id. """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class CustomJWTSerializer(JSONWebTokenSerializer,ModelBackend):
    username_field = 'email'

    def validate(self, attrs):
        credentials = {
            'email': attrs.get(self.username_field),
            'password': attrs.get('password')
        }
        print(credentials)

        if all(credentials.values()):
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            def authenticate( email=None, password=None, **kwargs):
                """ Authenticate a user based on email address as the user name. """
                try:
                    user = User.objects.get(email=email)
                    if user.check_password(password):
                        return user
                except User.DoesNotExist:
                    return None

            user = authenticate(**credentials)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)

                payload = jwt_payload_handler(user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "{username_field}" and "password".')
            msg = msg.format(username_field=self.username_field)
            raise serializers.ValidationError(msg)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')

def jwt_response_payload_handler(token, user=None, request=None):
    patient = Patient.objects.get(user=user)
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data,
        'patient': PatientSerializer(patient, context={'request': request}).data,
    }
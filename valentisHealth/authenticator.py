from django.db.models import Q


def is_labs(request):
    return request.user.groups.filter(
        Q(name='Labs') | Q(name='Callcenter') | Q(name='Admin') | Q(name='Superadmin')).exists()


def is_radiology(request):
    return request.user.groups.filter(
        Q(name='Radiologist') | Q(name='Callcenter') | Q(name='Admin') | Q(name='Superadmin')).exists()


def is_doctor(request):
    return request.user.groups.filter(
        Q(name='Doctor') | Q(name='Callcenter') | Q(name='Admin') | Q(name='Superadmin')).exists()


def is_callcenter(request):
    return request.user.groups.filter(Q(name='Callcenter') | Q(name='Admin') | Q(name='Superadmin')).exists()


def is_nurse(request):
    return request.user.groups.filter(
        Q(name='Nurse') | Q(name='Callcenter') | Q(name='Admin') | Q(name='Superadmin')).exists()


def is_receptionist(request):
    return request.user.groups.filter(
        Q(name='Receptionist') | Q(name='Callcenter') | Q(name='Admin') | Q(name='Superadmin')).exists()


def is_admin(request):
    return request.user.groups.filter(Q(name='Admin') | Q(name='Superadmin')).exists()


# def is_admin(request):
#     return self.request.user.groups.filter(Q(name='Admin') | Q(name='Superadmin')).exists()

def is_superadmin(request):
    return request.user.groups.filter(Q(name='Superadmin')).exists()




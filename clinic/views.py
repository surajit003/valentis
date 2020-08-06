from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import PatientVisit
from .forms import PatientVisitForm
from registration.models import Patient
from django.http import HttpResponseRedirect
from django.http import Http404
from nurse.models import Nurse
from tests.models import Labs, Radiology, RadiologyResult, LabResults
from tests.forms import labsForm, radiologyForm
from django.forms.models import model_to_dict
from medication.models import models as Medication
from django.contrib.auth.mixins import UserPassesTestMixin
from valentisHealth.authenticator import *
from django.http import JsonResponse

class PatientVisitListView(UserPassesTestMixin, ListView):
    model = PatientVisit

    def test_func(self):
        return is_doctor(self.request)

    def get_template_names(self):
        return 'clinic/visitform_list.html'

    def get_context_data(self, **kwargs):
        context = super(PatientVisitListView, self).get_context_data(**kwargs)

        try:
            context['all_patients'] = Patient.objects.all()

        except:
            raise Http404('Requested user not found.')

        return context


class PatientVisitCreateView(UserPassesTestMixin, CreateView):
    model = PatientVisit
    form_class = PatientVisitForm
    template_name = "clinic/clinic_landing.html"

    def test_func(self):
        return is_doctor(self.request)

    def get_context_data(self, **kwargs):
        # self.validate(self,request)
        context = super(PatientVisitCreateView, self).get_context_data(**kwargs)

        try:
            context['waiting_list'] = Patient.objects.filter(Q(status="3"))
        except:
            pass
        try:
            context['from_labs'] = Patient.objects.filter(Q(status="-4") | Q(status="-45"))
        except:
            pass
        try:
            context['from_radiology'] = Patient.objects.filter(Q(status="-5") | Q(status="-54"))
        except:
            pass

        context['link'] = 'clinic/patientvisit/doctor'
        context['clinic'] = True
        context['show_waiting_list'] = True

        return context


class PatientVisitDetailView(DetailView):
    model = PatientVisit


class PatientVisitUpdateView(UpdateView):
    model = PatientVisit
    form_class = PatientVisitForm


class Close(View):
    model = PatientVisit
    form_class = PatientVisitForm

    def get(self, request, *args, **kwargs):
        # fetch your values from request.GET.get('key')
        # and play around with it
        print("Succeeded")
        patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
        patient_object.status = 0
        patient_object.save()
        return JsonResponse({'success':'true', 'status':'true'}, status=200)


class DoctorVisit(UserPassesTestMixin, UpdateView):
    model = PatientVisit
    form_class = PatientVisitForm

    def test_func(self):
        return is_doctor(self.request)

    def get_object(self, queryset=None, **kwargs):
        patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
        session_id = patient_object.session_id

        try:

            visit_object = PatientVisit.objects.get(triage_id=session_id)
            visit_object.triage_id = session_id
            visit_object.save()
            print("exists -----------------------", session_id)
            print("exists -----------------------", visit_object.diag_search)

            return visit_object

        except:
            print("Did not exist +++++++++++++++++++++++++++", session_id)
            visit_object = PatientVisit.objects.create(triage_id=session_id)
            visit_object.triage_id = session_id
            visit_object.attending_doctor = self.request.user.email
            visit_object.save()
            return visit_object

    def get_template_names(self):
        return 'clinic/visitform_form.html'

    def form_valid(self, form):
        print ('form save')
        instance = form.save(commit=False)
        instance.save()

        return HttpResponseRedirect("/clinic/patientvisit/create/")

    def get_context_data(self, **kwargs):
        context = super(DoctorVisit, self).get_context_data(**kwargs)
        patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
        triage = Nurse.objects.filter(Q(patient_no=self.kwargs['patient_no']))[0]

        try:
            labresult = LabResults.objects.filter(Q(triage_id=patient_object.session_id))
            labtest = Labs.objects.filter(Q(triage_id=patient_object.session_id)).latest('created')
            context['lab_results'] = labresult
            context['lab_tests'] = labsForm(data=model_to_dict(labtest))

        except:
            pass

        try:
            radiologyresult = RadiologyResult.objects.filter(Q(triage_id=patient_object.session_id))
            radiologytest = Radiology.objects.filter(Q(triage_id=patient_object.session_id)).latest('created')
            context['radiology_results'] = radiologyresult
            context['radiology_test'] = radiologyForm(data=model_to_dict(radiologytest))
        except:
            pass


        try:

            context['waiting_list'] = Patient.objects.filter(status="3")
            context['triage'] = triage

            #-4 out of tests, -5 out of radiology
            context['from_labs'] = Patient.objects.filter(Q(status="-4") | Q(status="-45"))
            context['prev_visit'] = PatientVisit.objects.filter(Q(patient_no=self.kwargs['patient_no']))
            print ('Entered')
            print(context['prev_visit'])
            context['from_radiology'] = Patient.objects.filter(Q(status="-5") | Q(status="-54"))
            context['patient'] = patient_object

        except:
            print("Error ________")

        return context


class ClinicReport(ListView):
    model = PatientVisit

    def get_template_names(self):
        return 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ClinicReport, self).get_context_data(**kwargs)

        try:
            visit_obj = PatientVisit.objects.get(visit_id=self.kwargs['visit_id'])
            context['visit'] = visit_obj
            try:
                patient_object = Patient.objects.get(patient_no=visit_obj.patient_no)
                context['patient'] = patient_object
            except:
                pass
            try:
                prescription = Medication.objects.get(triage_id=visit_obj.triage_id)
                context['prescription'] = prescription
            except:
                pass
            try:
                triage = Nurse.objects.get(triage_id=visit_obj.triage_id)
                context['triage'] = triage
            except:
                pass
        except:
            pass

        return context

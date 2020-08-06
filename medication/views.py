from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from registration.models import Patient
from valentisHealth.authenticator import *
from .forms import MedicationForm
from .models import Medication
from valentisHealth.authenticator import *
from django.contrib.auth.mixins import UserPassesTestMixin

class MedicationListView(ListView):
    model = Medication


class MedicationCreateView(UserPassesTestMixin, CreateView):
    model = Medication
    form_class = MedicationForm

    def test_func(self):
        return is_nurse(self.request) or is_doctor(self.request) or is_callcenter(request)

    def form_valid(self, form):
        instance = form.save(commit=False)
        # status 4 means patient's in lab
        instance.status = 0
        try:
            patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
            instance.triage_id = patient_object.session_id
        except:
            pass
        instance.save()

        try:
            visit = patientVisit.objects.get(patient_no=self.kwargs['patient_no']).latest('created')
            prescr = models.objects.get(triage_id=self.kwargs['patient_no']).latest('created')
            visit.prescription_id = prescr.presscription_id
        except:
           pass

        return HttpResponseRedirect("/medication/search")

    def get_context_data(self, **kwargs):
        context = super(MedicationCreateView, self).get_context_data(**kwargs)

        try:
            patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
            patient_object.patient_name = patient_object.first_name + " " + patient_object.last_name
            context['patient'] = patient_object

        except:
            raise Http404('Requested user not found.')

        return context


class MedicationDetailView(UserPassesTestMixin, DetailView):
    model = Medication

    def test_func(self):
        return is_nurse(self.request) or is_doctor(self.request) or is_callcenter(request)



class MedicationUpdateView(UserPassesTestMixin, UpdateView):
    model = Medication
    form_class = Medication

    def test_func(self):
        return is_nurse(self.request) or is_doctor(self.request) or is_callcenter(request)


class MedicationSearchView(UserPassesTestMixin, View):
    model = Medication

    def test_func(self):
        return is_nurse(self.request) or is_doctor(self.request) or is_callcenter(request)

    # def get_template_names(self):
    #     return 'medication/medication_search.html'

    def get(self, request):

        return render(request, 'medication/medication_search.html')

class PrescriptionPdf(ListView):

    def test_func(self):
        return is_nurse(self.request) or is_doctor(self.request) or is_callcenter(request)

    # def get_template_names(self):
    #     return 'medication/medication_search.html'

    def get(self, request):
        return render(request, 'prescription_receipt.html')
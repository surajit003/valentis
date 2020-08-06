from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import Nurse
from .forms import ModelsForm
from registration.models import Patient
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.contrib.auth.mixins import UserPassesTestMixin
from valentisHealth.authenticator import *
from django.shortcuts import render

class ModelsListView(ListView):
    model = Nurse


class NurseLandingView(View):

    def get(self, request):
        context = {
            'waiting_list': Patient.objects.filter(status="2"),
            'link':'nurse/create',
            'show_waiting_list':True
        }

        return render(self.request, 'nurse/nurse_landing.html', context)


class NurseCreateView(UserPassesTestMixin, CreateView):
    model = Nurse
    form_class = ModelsForm

    def test_func(self):
        return is_nurse(self.request) or is_doctor(self.request)

    def get_context_data(self, **kwargs):
        context = super(NurseCreateView, self).get_context_data(**kwargs)
        context['waiting_list'] = Patient.objects.filter(status="2")
        context['patient'] = Patient.objects.get(patient_no=self.kwargs['patient_no'])
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.attending_nurse =  self.request.user.get_full_name()+ " " + self.request.user.email

        try:
            patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
            patient_object.status = 3
            patient_object.session_id = instance.triage_id
            patient_object.save()

            instance.patient = patient_object
            instance.patient_no = patient_object.patient_no
        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        return HttpResponseRedirect("/nurse/nurse")


class NurseDetailView(UserPassesTestMixin, DetailView):
    model = Nurse

    def test_func(self):
        return is_nurse(self.request) or is_doctor(self.request)


class NurseUpdateView(UserPassesTestMixin, UpdateView):
    model = Nurse
    form_class = ModelsForm

    def test_func(self):
        return is_nurse(self.request) or is_doctor(self.request)


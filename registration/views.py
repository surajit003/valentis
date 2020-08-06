from django.views.generic import ListView, UpdateView, CreateView, View, DetailView
from .models import Patient, Child
from .forms import PatientForm
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, reverse
from django.shortcuts import render
from django.forms import inlineformset_factory
# from django.contrib.auth.mixins import UserPassesTestMixin
# from valentisHealth.authenticator import *
from django.contrib import messages

class LandingView(ListView):
    model = Patient

    def get_template_names(self):
        return 'registration/search_patient.html'


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm

    def get_context_data(self, **kwargs):
        context = super(PatientCreateView, self).get_context_data(**kwargs)
        context['new'] = True

        return context

    def get_template_names(self):
        print("+++____+++___+++", self.request.POST.dict())
        return 'registration/patient_form.html'

    def form_valid(self, form):

        instance = form.save(commit=False)
        instance.status = 0
        errors_check = instance.create_patient_account(self.request)
        instance.save()

        if errors_check:
            print('error occurred', errors_check)
            return render(self.request, 'registration/patient_form.html', {'errors': errors_check,'new':True, 'form':form})



        message = "Successfully created patient and patient account. Login detail for the mobile app are sent to their email"

        messages.add_message(self.request, messages.INFO, message)

        return HttpResponseRedirect('/registration')


class PatientDetailView(DetailView):
    def get_object(self, queryset=None, **kwargs):
        patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])

        return patient_object

    def get_template_names(self):
        return 'registration/history_form.html'

    # def get_object(self):
    #     return get_object_or_404(models, pk=request.session['user_id'])

    def get_context_data(self, **kwargs):
        context = super(PatientDetailView, self).get_context_data(**kwargs)
        try:
            patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
            context['patient'] = patient_object

        except:
            raise Http404('Requested user not found.')

        return context

class SendToTriageView(View):
    template_name = 'registration/search_patient.html'
    def get(self, request, *args, **kwargs):
        patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
        if int(patient_object.status)>1:
            return render(self.request, self.template_name, {"errors":"This patient ("+patient_object.full_name()+") is still under treatment", "patient":patient_object})
        else:
            patient_object.status = 2
            patient_object.save()

            return render(self.request, self.template_name, {"success":"Patient has been sent to triage", "patient":patient_object})

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'registration/patient_form.html'

    def get_object(self, **kwargs):
        patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])

        return patient_object

    def form_valid(self, form):
        patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
        instance = form.save(commit=False)
        instance.status = patient_object.status
        instance.user = patient_object.user
        instance.session_id = patient_object.session_id
        instance.save()

        context = self.get_context_data()
        child_form = context['child_formset']
        if child_form.is_valid():
            self.object = form.save()
            child_form.instance = self.object
            child_form.save()

        return render(self.request, self.template_name, {'form': form, 'success':"Updated the patient's history successfully", 'child_formset':child_form})

    def get_context_data(self, **kwargs):
        context = super(PatientUpdateView, self).get_context_data(**kwargs)
        patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
        context['patient'] = patient_object

        ChildFormSet = inlineformset_factory(Patient, Child, exclude=())
        if self.request.POST:
            context['child_formset'] = ChildFormSet(self.request.POST)
        else:
            context['child_formset'] = ChildFormSet()

        return context

from django.views.generic import DetailView, ListView, UpdateView, CreateView, View
from .models import Labs, Radiology, RadiologyResult, LabResults
from .forms import labsForm, radiologyForm, RadiologyResultForm, LabResultsForm
from django.http import HttpResponseRedirect, JsonResponse
from registration.models import Patient
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render #, get_object_or_404, redirect, reverse
from django.forms.models import model_to_dict
from django.db.models import Q
from rest_framework import generics
from .serializers import LabResultsSerializer, RadiologyResultSerializer
from valentisHealth.authenticator import *
from django.contrib.auth.mixins import UserPassesTestMixin

class LabsLanding(UserPassesTestMixin, ListView):
    model = Labs

    def test_func(self):
        return is_labs(self.request) or is_doctor(self.request)

    def get_template_names(self):
        return 'tests/labs_list.html'

    def get_context_data(self, **kwargs):
        pass
        context = super(LabsLanding, self).get_context_data(**kwargs)

        try:
            #get patients in tests (status 4)
            context['waiting_list'] = Patient.objects.filter(Q(status="4") | Q(status="45") | Q(status='-54'))
            context['show_waiting_list'] = True

            #sent link to be appended to the href in waiting list table row accounts/templates/base
            context['link'] = 'tests/labresults/new'

        except:
            raise Http404('Requested user not found.')

        return context


class LabsCreateView(UserPassesTestMixin,CreateView):
    model = Labs
    form_class = labsForm

    def test_func(self):
        return is_labs(self.request) or is_doctor(self.request)

    def get_template_names(self):
        return 'lab/labs_form.html'


    def form_valid(self, form):
        instance = form.save(commit=False)

        instance.attending_doc = self.request.user.email

        try:
            patient_object = Patient.objects.get(patient_no=form.cleaned_data['patient_no'])

            #if patient is in radiology
            if patient_object.status == 5:
                # 45 means patient is in both tests and Radiology
                patient_object.status = 45
            else:
                patient_object.status = 4

            patient_object.save()
        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        return HttpResponseRedirect("/clinic/patientvisit/create/")


class LabsDetailView(UserPassesTestMixin, DetailView):
    model = Labs

    def test_func(self):
        return is_labs(self.request) or is_doctor(self.request)


class LabsUpdateView(UserPassesTestMixin, UpdateView):
    model = Labs
    form_class = labsForm

    def test_func(self):
        return is_labs(self.request) or is_doctor(self.request)


class RadiologyListView(UserPassesTestMixin, ListView):
    model = Radiology

    def get_template_names(self):
        return 'tests/radiology_list.html'

    def test_func(self):
        return is_radiology(self.request) or is_doctor(self.request)

    def get_context_data(self, **kwargs):
        context = super(RadiologyListView, self).get_context_data(**kwargs)

        try:
            #get patient's in radiology (staus 5)
            context['waiting_list'] = Patient.objects.filter(Q(status="5") | Q(status="45") | Q(status="-45"))

            context['show_waiting_list'] = True
            context['link'] = 'tests/radiologyresult/new'
        except:
            raise Http404('Requested user not found.')

        return context


class RadiologyCreateView(UserPassesTestMixin, CreateView):
    model = Radiology
    form_class = radiologyForm

    def test_func(self):
        return is_radiology(self.request) or is_doctor(self.request)

    def get_template_names(self):
        return 'tests/radiology_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)

        instance.attending_doc = self.request.user.email

        try:
            patient_object = Patient.objects.get(patient_no=form.cleaned_data['patient_no'])

            # if patient is in tests
            if patient_object.status == 4:
                # 45 means patient is in both tests and Radiology
                patient_object.status = 45
            else:
                patient_object.status = 5

            patient_object.save()
        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        return HttpResponseRedirect("/clinic/patientvisit/create/")


class RadiologyDetailView(UserPassesTestMixin, DetailView):
    model = Radiology

    def test_func(self):
        return is_radiology(self.request) or is_doctor(self.request)

class RadiologyUpdateView(UserPassesTestMixin, UpdateView):
    model = Radiology
    form_class = radiologyForm

    def test_func(self):
        return is_radiology(self.request) or is_doctor(self.request)


class RadiologyResultListView(UserPassesTestMixin, ListView):
    model = RadiologyResult

    def test_func(self):
        return is_radiology(self.request) or is_doctor(self.request)


class RadiologyResultDetailView(UserPassesTestMixin, DetailView):
    model = RadiologyResult

    def test_func(self):
        return is_radiology(self.request) or is_doctor(self.request)


class RadiologyResultUpdateView(UserPassesTestMixin, UpdateView):
    model = RadiologyResult
    form_class = RadiologyResultForm

    def test_func(self):
        return is_radiology(self.request) or is_doctor(self.request)


class LabResultsListView(UserPassesTestMixin, ListView):
    model = LabResults

    def test_func(self):
        return is_labs(self.request) or is_doctor(self.request)


class LabResultsDetailView(UserPassesTestMixin, DetailView):
    model = LabResults

    def test_func(self):
        return is_labs(self.request) or is_doctor(self.request)


class LabResultsUpdateView(UserPassesTestMixin, UpdateView):
    model = LabResults
    form_class = LabResultsForm

    def test_func(self):
        return is_labs(self.request) or is_doctor(self.request)


class LabsVisitView(UserPassesTestMixin, CreateView):
    model = LabResults
    form_class = labsForm

    def test_func(self):
        return is_labs(self.request) or is_doctor(self.request)

    def get_template_names(self):
        return 'tests/labresult_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.attending_nurse = self.request.user.email

        try:
            print(form.cleaned_data['patient_no'])
            patient_object = Patient.objects.get(patient_no=form.cleaned_data['patient_no'])

            #status -45 patient is out of tests but in radiology
            if patient_object.status==45:
                patient_object.status = -45

            else:
                #patient out of tests
                patient_object.status=-4

            patient_object.save()
        except:
            print(404)
            raise Http404('Requested user not found.')

        instance.save()

        return HttpResponseRedirect("/tests/labs/")

    def get_context_data(self, **kwargs):

        context = super(LabsVisitView, self).get_context_data(**kwargs)

        try:
            patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
            context['patient'] = patient_object
            lab_object = Labs.objects.filter(triage_id=patient_object.session_id).latest('created')
            object = labsForm(data=model_to_dict(lab_object))
            context['request_'] = object
            context['other'] = lab_object.other #text area field in the labresult form
            context['diagnosis'] = lab_object.diagnosis
        except:
            raise Http404('Requested user not found.')

        return context


class RadiologyVisitView(UserPassesTestMixin, CreateView):
    model = RadiologyResult
    form_class = RadiologyResultForm

    def test_func(self):
        return is_labs(self.request) or is_doctor(self.request)

    def get_template_names(self):
        return 'tests/radiology_result_form.html'

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.attending_nurse = self.request.user.email

        try:
            patient_object = Patient.objects.get(patient_no=form.cleaned_data['patient_no'])

            # status -54 patient is out of tests but in radiology
            if patient_object.status == 45:
                patient_object.status = -54
            else:
                # patient out of tests
                patient_object.status = -5

            patient_object.save()

        except:
            print(404)
            raise Http404('Could not complete operations.')

        instance.save()

        return HttpResponseRedirect("/tests/radiology")

    def get_context_data(self, **kwargs):

        context = super(RadiologyVisitView, self).get_context_data(**kwargs)

        try:
            patient_object = Patient.objects.get(patient_no=self.kwargs['patient_no'])
            context['patient'] = patient_object
            radiology_object = Radiology.objects.filter(triage_id=patient_object.session_id).latest('created')

            object = radiologyForm(data=model_to_dict(radiology_object))
            context['request_'] = object
            context['examination'] = radiology_object.examination
            context['clinical_indication'] = radiology_object.clinical_indication
            # print(object)

        except:
            raise Http404('Requested user not found.')

        return context


# def Tests(request, triage_id):
#     return JsonResponse()

class Tests(generics.GenericAPIView):
    def test_func(self):
        return is_labs(self.request) or is_doctor(self.request)

    def get(self, request, *args, **kwargs):
        labresult = LabResults.objects.filter(triage_id=kwargs.get('triage_id'))
        radiologyresult = RadiologyResult.objects.filter(triage_id=kwargs.get('triage_id'))

        context = {
            "request": request,
        }

        labs_serializer = LabResultsSerializer(labresult, many=True, context=context)
        radiology_serializer = RadiologyResultSerializer(radiologyresult, many=True, context=context)

        response = labs_serializer.data + radiology_serializer.data

        return JsonResponse(response)
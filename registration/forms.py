from django import forms
from .models import Patient, Child
from django.forms import Textarea
from django.forms.formsets import BaseFormSet


class PatientForm(forms.ModelForm):
    IDCHOICES = (
        ('ID', 'ID Number'),
        ('Passport', 'Passport Number'),
    )

    IDOCCHOICES = (
        ('ID', 'ID Number'),
        ('Passport', 'Passport Number'),
    )

    id_type = forms.CharField(widget=forms.Select(choices=IDCHOICES, attrs={
        'class': 'select-box',
    }), required=False,)

    id_type_sub = forms.CharField(widget=forms.Select(choices=IDOCCHOICES, attrs={
        'class': 'select-box',
    }), required=False, )

    GENDERCHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    gender = forms.CharField(widget=forms.Select(choices=GENDERCHOICES,
                                                 attrs={
                                                     'class': 'select-box',
                                                 }
                                                 ))

    dob = forms.DateField(widget=forms.TextInput(
        attrs={
            'class': 'mdl-textfield__input',
            'type': 'date',
            'onkeyup': 'setDob($(this).val())',
            'onchange': 'setDob($(this).val())'

        }
    ))


    YESNOCHOICES = (
        ('--', '--'),
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    pri_ins_sub = forms.CharField(required=False, widget=forms.Select(choices=YESNOCHOICES,
                                                                               attrs={
                                                                                   'class': 'select-box',
                                                                               }
                                                                               ))

    sec_ins_sub = forms.CharField(required=False, widget=forms.Select(choices=YESNOCHOICES,
                                                                      attrs={
                                                                          'class': 'select-box',
                                                                      }
                                                                      ))

    if_smoker = forms.CharField(required=False,widget=forms.Select(choices=YESNOCHOICES,
                                                 attrs={
                                                     'class': 'select-box',
                                                 }
                                                 ))
    if_quit_before = forms.CharField(required=False,widget=forms.Select(choices=YESNOCHOICES,
                                                 attrs={
                                                     'class': 'select-box',
                                                 }
                                                 ))

    if_chew_tobacco = forms.CharField(required=False,widget=forms.Select(choices=YESNOCHOICES,
                                                    attrs={
                                                        'class': 'select-box',
                                                    }
                                                    ))


    if_drink_alcohol = forms.CharField(required=False,widget=forms.Select(choices=YESNOCHOICES,
                                                  attrs={
                                                      'class': 'select-box',
                                                  }
                                                  ))

    if_drug_used = forms.CharField(required=False,widget=forms.Select(choices=YESNOCHOICES,
                                                           attrs={
                                                               'class': 'select-box',
                                                           }
                                                           ))

    if_exercise = forms.CharField(required=False,widget=forms.Select(choices=YESNOCHOICES,
                                                      attrs={
                                                          'class': 'select-box',
                                                      }
                                                      ))

    if_special_diet = forms.CharField(required=False,widget=forms.Select(choices=YESNOCHOICES,
                                                      attrs={
                                                          'class': 'select-box',
                                                      }
                                                      ))

    if_use_caffein = forms.CharField(required=False,widget=forms.Select(choices=YESNOCHOICES,
                                                          attrs={
                                                              'class': 'select-box',
                                                          }
                                                          ))

    is_sadder = forms.CharField(required=False,widget=forms.Select(choices=YESNOCHOICES,
                                                              attrs={
                                                                  'class': 'select-box',
                                                              }
                                                              ))

    if_lost_interest = forms.CharField(required=False,widget=forms.Select(choices=YESNOCHOICES,
                                                              attrs={
                                                                  'class': 'select-box',
                                                              }
                                                              ))

    have_will = forms.CharField(required=False,widget=forms.Select(choices=YESNOCHOICES,
                                                              attrs={
                                                                  'class': 'select-box',
                                                              }
                                                              ))
    MARITALSTATUS = (
        ('Single','Single'),
        ('Married','Married'),
        ('Divorced','Divorced'),
    )

    marital_status = forms.CharField(required=False,widget=forms.Select(choices=MARITALSTATUS,
                                                              attrs={
                                                                  'class': 'select-box',
                                                              }
                                                              ))


    sub_dob = forms.DateField(label='Date of Birth',
                              required=False,
                              widget=forms.DateInput(
                                  attrs={
                                      'class': 'mdl-textfield__input',
                                      'type': 'date'
                                  }
                              ))
    last_phys_examination = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'mdl-textfield__input',
                'type': 'date'
            }
        ))

    last_blood_work = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'mdl-textfield__input',
                'type': 'date'
            }
        ))

    last_colonoscopy = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'mdl-textfield__input',
                'type': 'date'
            }
        ))

    last_tetanus_shot = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'mdl-textfield__input',
                'type': 'date'
            }
        ))

    last_menstrual = forms.DateField(
        input_formats=['m-d-Y'],
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'mdl-textfield__input',
                'type': 'date'
            }
        ))

    last_pap_smear = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'mdl-textfield__input',
                'type': 'date'
            }
        ))

    abnormal_pap = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'mdl-textfield__input',
                'type': 'date'
            }
        ))

    last_mammogram = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'mdl-textfield__input',
                'type': 'date'
            }
        ))

    dexa = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'mdl-textfield__input',
                'type': 'date'
            }
        ))


    class Meta:
        model = Patient

        exclude = ('patient_no', 'created')


class MedicationForm(forms.Form):
    medication = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Medication',
        }),
        required=False)
    dosage = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Dosage',
        }))

    route = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Route',
        }))

    frequency = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'frequency',
        }))

    patient_no = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'placeholder': 'Patient ID',
        }))


class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['child_name', 'child_age', 'child_dob']


class MedicationFormSet(BaseFormSet):
    def clean(self):

        if any(self.errors):
            return

        for form in self.forms:
            if form.cleaned_data:
                dosage = form.cleaned_data['dosage']
                medication = form.cleaned_data['medication']
                route = form.cleaned_data['route']
                frequency = form.cleaned_data['frequency']

                # Check that all links have both an anchor and URL
                if (dosage and not medication) or (route and not medication) or (frequency and not medication):
                    raise forms.ValidationError(
                        'You must enter a medication.',
                        code='missing_medication'
                    )

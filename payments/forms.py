from django import forms
from .models import member_info, member_benefits, member_anniversary, member_acceptance, principal_applicant, pre_authorization, provider, cash
from django.contrib.admin.widgets import AdminDateWidget

from .models import WARD

# from . import demo as forms
# from material import Layout, Row, Column, Fieldset, Span2, Span3, Span5, Span6, Span10


COUNTRY_CHOICES = (
    ('', 'Country'), (244, 'Aaland Islands'), (1, 'Afghanistan'), (2, 'Albania'), (3, 'Algeria'),
    (4, 'American Samoa'), (5, 'Andorra'), (6, 'Angola'), (7, 'Anguilla'), (8, 'Antarctica'),
    (9, 'Antigua and Barbuda'), (10, 'Argentina'), (11, 'Armenia'), (12, 'Aruba'), (13, 'Australia'),
    (14, 'Austria'), (15, 'Azerbaijan'), (16, 'Bahamas'), (17, 'Bahrain'), (18, 'Bangladesh'),
    (19, 'Barbados'), (20, 'Belarus'), (21, 'Belgium'), (22, 'Belize'), (23, 'Benin'),
    (24, 'Bermuda'), (25, 'Bhutan'), (26, 'Bolivia'), (245, 'Bonaire, Sint Eustatius and Saba'),
    (27, 'Bosnia and Herzegovina'), (28, 'Botswana'), (29, 'Bouvet Island'), (30, 'Brazil'),
    (31, 'British Indian Ocean Territory'), (32, 'Brunei Darussalam'),
    (33, 'Bulgaria'), (34, 'Burkina Faso'), (35, 'Burundi'), (36, 'Cambodia'), (37, 'Cameroon'),
    (38, 'Canada'), (251, 'Canary Islands'), (39, 'Cape Verde'), (40, 'Cayman Islands'), (41, 'Central African Republic'),
    (42, 'Chad'), (43, 'Chile'), (44, 'China'), (45, 'Christmas Island'), (46, 'Cocos (Keeling) Islands'),
    (47, 'Colombia'), (48, 'Comoros'), (49, 'Congo'), (50, 'Cook Islands'), (51, 'Costa Rica'),
    (52, "Cote D'Ivoire"), (53, 'Croatia'), (54, 'Cuba'), (246, 'Curacao'), (55, 'Cyprus'),
    (56, 'Czech Republic'), (237, 'Democratic Republic of Congo'), (57, 'Denmark'), (58, 'Djibouti'), (59, 'Dominica'),
    (60, 'Dominican Republic'), (61, 'East Timor'), (62, 'Ecuador'), (63, 'Egypt'), (64, 'El Salvador'),
    (65, 'Equatorial Guinea'), (66, 'Eritrea'), (67, 'Estonia'), (68, 'Ethiopia'), (69, 'Falkland Islands (Malvinas)'),
    (70, 'Faroe Islands'), (71, 'Fiji'), (72, 'Finland'), (74, 'France, skypolitan'), (75, 'French Guiana'),
    (76, 'French Polynesia'), (77, 'French Southern Territories'), (126, 'FYROM'), (78, 'Gabon'), (79, 'Gambia'),
    (80, 'Georgia'), (81, 'Germany'), (82, 'Ghana'), (83, 'Gibraltar'), (84, 'Greece'),
    (85, 'Greenland'), (86, 'Grenada'), (87, 'Guadeloupe'), (88, 'Guam'), (89, 'Guatemala'),
    (241, 'Guernsey'), (90, 'Guinea'), (91, 'Guinea-Bissau'), (92, 'Guyana'), (93, 'Haiti'),
    (94, 'Heard and Mc Donald Islands'), (95, 'Honduras'), (96, 'Hong Kong'), (97, 'Hungary'), (98, 'Iceland'),
    (99, 'India'), (100, 'Indonesia'), (101, 'Iran (Islamic Republic of)'), (102, 'Iraq'), (103, 'Ireland'),
    (104, 'Israel'), (105, 'Italy'), (106, 'Jamaica'), (107, 'Japan'), (240, 'Jersey'),
    (108, 'Jordan'), (109, 'Kazakhstan'), (110, 'Kenya'), (111, 'Kiribati'), (113, 'Korea, Republic of'),
    (114, 'Kuwait'), (115, 'Kyrgyzstan'), (116, "Lao People's Democratic Republic"), (117, 'Latvia'), (118, 'Lebanon'),
    (119, 'Lesotho'), (120, 'Liberia'), (121, 'Libyan Arab Jamahiriya'), (122, 'Liechtenstein'), (123, 'Lithuania'),
    (124, 'Luxembourg'), (125, 'Macau'), (127, 'Madagascar'), (128, 'Malawi'), (129, 'Malaysia'),
    (130, 'Maldives'), (131, 'Mali'), (132, 'Malta'), (133, 'Marshall Islands'), (134, 'Martinique'),
    (135, 'Mauritania'), (136, 'Mauritius'), (137, 'Mayotte'), (138, 'Mexico'), (139, 'Micronesia, Federated States of'),
    (140, 'Moldova, Republic of'), (141, 'Monaco'), (142, 'Mongolia'), (242, 'Montenegro'), (143, 'Montserrat'),
    (144, 'Morocco'), (145, 'Mozambique'), (146, 'Myanmar'), (147, 'Namibia'), (148, 'Nauru'),
    (149, 'Nepal'), (150, 'Netherlands'), (151, 'Netherlands Antilles'), (152, 'New Caledonia'), (153, 'New Zealand'),
    (154, 'Nicaragua'), (155, 'Niger'), (156, 'Nigeria'), (157, 'Niue'), (158, 'Norfolk Island'),
    (112, 'North Korea'), (159, 'Northern Mariana Islands'), (160, 'Norway'), (161, 'Oman'), (162, 'Pakistan'),
    (163, 'Palau'), (247, 'Palestinian Territory, Occupied'), (164, 'Panama'), (165, 'Papua New Guinea'), (166, 'Paraguay'),
    (167, 'Peru'), (168, 'Philippines'), (169, 'Pitcairn'), (170, 'Poland'), (171, 'Portugal'),
    (172, 'Puerto Rico'), (173, 'Qatar'), (174, 'Reunion'), (175, 'Romania'), (176, 'Russian Federation'),
    (177, 'Rwanda'), (178, 'Saint Kitts and Nevis'), (179, 'Saint Lucia'), (180, 'Saint Vincent and the Grenadines'),
    (181, 'Samoa'), (182, 'San Marino'), (183, 'Sao Tome and Principe'), (184, 'Saudi Arabia'), (185, 'Senegal'),
    (243, 'Serbia'), (186, 'Seychelles'), (187, 'Sierra Leone'), (188, 'Singapore'), (189, 'Slovak Republic'),
    (190, 'Slovenia'), (191, 'Solomon Islands'), (192, 'Somalia'), (193, 'South Africa'),
    (194, 'South Georgia &amp; South Sandwich Islands'), (248, 'South Sudan'), (195, 'Spain'), (196, 'Sri Lanka'),
    (249, 'St. Barthelemy'), (197, 'St. Helena'), (250, 'St. Martin (French part)'), (198, 'St. Pierre and Miquelon'),
    (199, 'Sudan'), (200, 'Suriname'), (201, 'Svalbard and Jan Mayen Islands'), (202, 'Swaziland'),
    (203, 'Sweden'), (204, 'Switzerland'), (205, 'Syrian Arab Republic'), (206, 'Taiwan'), (207, 'Tajikistan'),
    (208, 'Tanzania, United Republic of'), (209, 'Thailand'), (210, 'Togo'), (211, 'Tokelau'), (212, 'Tonga'),
    (213, 'Trinidad and Tobago'), (214, 'Tunisia'), (215, 'Turkey'), (216, 'Turkmenistan'),
    (217, 'Turks and Caicos Islands'), (218, 'Tuvalu'), (219, 'Uganda'), (220, 'Ukraine'), (221, 'United Arab Emirates'),
    (222, 'United Kingdom'), (223, 'United States'), (224, 'United States Minor Outlying Islands'), (225, 'Uruguay'),
    (226, 'Uzbekistan'), (227, 'Vanuatu'), (228, 'Vatican City State (Holy See)'), (229, 'Venezuela'), (230, 'Viet Nam'),
    (231, 'Virgin Islands (British)'), (232, 'Virgin Islands (U.S.)'), (233, 'Wallis and Futuna Islands'),
    (234, 'Western Sahara'), (235, 'Yemen'), (238, 'Zambia'), (239, 'Zimbabwe'),
)

class member_infoForm(forms.ModelForm):
    class Meta:
        model = member_info
        fields = ['family_no', 'member_no', 'surname', 'first_name', 'other_name', 'dob', 'user_id', 'date_entered', 'cancelled', 'employment_no', 'gender', 'passport_no']


class member_benefitsForm(forms.ModelForm):
    class Meta:
        model = member_benefits
        fields = ['name', 'member_no', 'limit', 'sharing', 'anniv', 'suspended', 'expense', 'idx', 'balance']


class member_anniversaryForm(forms.ModelForm):
    class Meta:
        model = member_anniversary
        fields = ['name', 'member_no', 'start_date', 'end_date', 'anniv']


class member_acceptanceForm(forms.ModelForm):
    class Meta:
        model = member_acceptance
        fields = ['name', 'member_no', 'status', 'status_date', 'user_id', 'date_entered']


class principal_applicantForm(forms.ModelForm):
    class Meta:
        model = principal_applicant
        fields = ['name', 'family_no', 'first_name', 'postal_add', 'town', 'email', 'other_names', 'corp_id', 'mobile_no', 'family_size', 'user_id', 'category']


class DateInput(forms.DateInput):
    input_type = 'date'

class pre_authorizationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(pre_authorizationForm, self).__init__(*args, **kwargs)
        # Making name required
        self.fields['date_admitted'].required = False

    class Meta:
        model = pre_authorization

        fields = ['name', 'member_no', 'provider','date_reported', 'reported_by', 'authorized_by',
                  'pre_diagnosis', 'authority_type', 'ward', 'available_limit', 'admit_days', 'reserve',
                  'internal_notes',
                  'notes', 'day_bed_charge', 'date_admitted', 'code']

        widgets = {
            'pre-diagnosis': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'date_reported': DateInput(),
            'date_admitted': DateInput(),
            'ward': forms.Select(attrs={
                'class': 'mdl-selectfield__select'
            }),
            'provider': forms.Select(attrs={
                'class': 'mdl-selectfield__select'
            })
        }

class providerForm(forms.ModelForm):
    class Meta:
        model = provider
        fields = ['name', 'code', 'provider']


class cashForm(forms.ModelForm):
    class Meta:
        model = cash
        fields = ['name', 'items', 'amount_payed', 'total_cost', 'balance']



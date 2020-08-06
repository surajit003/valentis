from django.core.mail import send_mail

import cgi
form = cgi.FieldStorage()
#{"patientnumber":patientnumber,"patientname":patientname,"phonenumber":phonenumber,"email":email,"address":address,
   #      "prescriptionid":prescriptionid};

patientnumber = form.getvalue("patientnumber","error")
def sendingemail(body):
    return(send_mail('Prescription',patientnumber,'surajit@redpulse.co.ke','smartsurajit2008@gmail.com',fail_silently=False,))
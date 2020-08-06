import os, csv
path =  "/opt/valentisHealth"
os.chdir(path)
from payments.models import member_info
with open('memberdata.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = member_info.objects.create(family_no=row['FAMILY_NO'], date_entered=row['DATE_ENTERED'], gender=row['gender'],passport_no=row['passport_no'], member_no=row['MEMBER_NO'], first_name=row['FIRST_NAME'], surname=row['SURNAME'], other_name=row['OTHER_NAMES'], dob=row['DOB'], user_id=row['USER_ID'], cancelled=row['CANCELLED'])
        p.save()


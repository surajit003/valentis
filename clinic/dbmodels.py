import os, csv

path ="/opt/demovalentisHealth"

os.chdir(path)
from clinic.models import Diagnosis

with open('icd.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        p = Diagnosis.objects.create(code=row['CODE'],name=row['NAME'])
        p.save()
